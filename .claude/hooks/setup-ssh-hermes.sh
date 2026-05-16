#!/usr/bin/env bash
# SessionStart hook: rebuild SSH access to the Hermes VPS from env vars.
# Exits silently when env vars are missing so non-Hermes sessions are unaffected.

set -euo pipefail

[[ -n "${HERMES_SSH_PRIVATE_KEY:-}" ]] || exit 0
[[ -n "${HERMES_HOST:-}" ]] || exit 0
[[ -n "${HERMES_USER:-}" ]] || exit 0

HERMES_PORT="${HERMES_PORT:-22}"
SSH_DIR="$HOME/.ssh"
KEY_PATH="$SSH_DIR/hermes_claude"
CONFIG_PATH="$SSH_DIR/config"

mkdir -p "$SSH_DIR"
chmod 700 "$SSH_DIR"

printf '%b' "$HERMES_SSH_PRIVATE_KEY" > "$KEY_PATH"
chmod 600 "$KEY_PATH"

if ! grep -q "^Host hermes$" "$CONFIG_PATH" 2>/dev/null; then
    cat >> "$CONFIG_PATH" <<EOF

Host hermes
    HostName ${HERMES_HOST}
    User ${HERMES_USER}
    Port ${HERMES_PORT}
    IdentityFile ${KEY_PATH}
    IdentitiesOnly yes
    StrictHostKeyChecking accept-new
    ServerAliveInterval 60
    ServerAliveCountMax 3
EOF
    chmod 600 "$CONFIG_PATH"
fi

echo "Hermes SSH configured: ssh hermes"
