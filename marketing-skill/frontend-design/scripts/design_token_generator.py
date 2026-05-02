#!/usr/bin/env python3
"""Generate CSS custom properties and design token JSON from structured data."""

import json
import argparse
from pathlib import Path
from typing import Dict, Any


def generate_css_variables(tokens: Dict[str, Any]) -> str:
    """Convert design tokens to CSS custom properties."""
    css_lines = [":root {"]

    def flatten_tokens(obj: Dict, prefix: str = ""):
        for key, value in obj.items():
            if isinstance(value, dict):
                flatten_tokens(value, f"{prefix}{key}-")
            else:
                var_name = f"--{prefix}{key}".lower()
                css_lines.append(f"  {var_name}: {value};")

    flatten_tokens(tokens)
    css_lines.append("}")
    return "\n".join(css_lines)


def generate_js_export(tokens: Dict[str, Any]) -> str:
    """Convert design tokens to JavaScript export."""
    return f"export const designTokens = {json.dumps(tokens, indent=2)};"


def generate_tailwind_config(tokens: Dict[str, Any]) -> str:
    """Generate Tailwind CSS configuration from design tokens."""
    config = {
        "theme": {
            "extend": tokens
        }
    }
    return f"module.exports = {json.dumps(config, indent=2)};"


def main():
    parser = argparse.ArgumentParser(
        description="Generate CSS custom properties and design token formats"
    )
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Input JSON file with design tokens"
    )
    parser.add_argument(
        "--output-format",
        choices=["css", "js", "tailwind", "all"],
        default="all",
        help="Output format"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=".",
        help="Output directory"
    )

    args = parser.parse_args()

    try:
        with open(args.input) as f:
            tokens = json.load(f)

        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        if args.output_format in ["css", "all"]:
            css_output = generate_css_variables(tokens)
            css_file = output_dir / "tokens.css"
            css_file.write_text(css_output)
            print(f"✓ Generated {css_file}")

        if args.output_format in ["js", "all"]:
            js_output = generate_js_export(tokens)
            js_file = output_dir / "tokens.js"
            js_file.write_text(js_output)
            print(f"✓ Generated {js_file}")

        if args.output_format in ["tailwind", "all"]:
            tailwind_output = generate_tailwind_config(tokens)
            tailwind_file = output_dir / "tailwind.config.js"
            tailwind_file.write_text(tailwind_output)
            print(f"✓ Generated {tailwind_file}")

        print(f"\nProcessed {len(tokens)} token categories")

    except FileNotFoundError:
        print(f"Error: Input file '{args.input}' not found")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{args.input}'")
        exit(1)


if __name__ == "__main__":
    main()
