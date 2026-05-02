#!/usr/bin/env python3
"""Calculate optimal responsive design breakpoints for mobile-first design."""

import json
import argparse
from typing import List, Dict


# Common device breakpoints (mobile-first approach)
DEVICE_BREAKPOINTS = {
    "xs": {"min": 0, "max": 480, "label": "Extra Small (Mobile Phone)"},
    "sm": {"min": 481, "max": 768, "label": "Small (Tablet Portrait)"},
    "md": {"min": 769, "max": 1024, "label": "Medium (Tablet Landscape)"},
    "lg": {"min": 1025, "max": 1440, "label": "Large (Desktop)"},
    "xl": {"min": 1441, "max": 1920, "label": "Extra Large (Large Desktop)"},
    "2xl": {"min": 1921, "max": 999999, "label": "2XL (Ultra Wide)"},
}

# Design system breakpoints (common frameworks)
DESIGN_SYSTEM_PRESETS = {
    "bootstrap": {
        "sm": 576,
        "md": 768,
        "lg": 992,
        "xl": 1200,
        "xxl": 1400
    },
    "tailwind": {
        "sm": 640,
        "md": 768,
        "lg": 1024,
        "xl": 1280,
        "2xl": 1536
    },
    "material": {
        "xs": 0,
        "sm": 600,
        "md": 960,
        "lg": 1264,
        "xl": 1904
    },
    "fluid": {
        "xs": 320,
        "sm": 640,
        "md": 1024,
        "lg": 1280,
        "xl": 1920
    }
}


def generate_mobile_first_breakpoints(max_width: int = 1920) -> Dict[str, int]:
    """Generate mobile-first breakpoints up to max width."""
    breakpoints = {}

    # Common mobile-first breakpoints
    candidates = [320, 480, 640, 768, 1024, 1280, 1440, 1600, 1920]

    for bp in candidates:
        if bp <= max_width:
            if bp <= 480:
                breakpoints[f"mobile"] = bp
            elif bp <= 768:
                breakpoints[f"tablet"] = bp
            elif bp <= 1024:
                breakpoints[f"tablet-lg"] = bp
            elif bp <= 1440:
                breakpoints[f"desktop"] = bp
            else:
                breakpoints[f"desktop-xl"] = bp

    return {k: v for k, v in sorted(breakpoints.items(), key=lambda x: x[1])}


def calculate_viewport_distribution(breakpoints: Dict[str, int]) -> Dict[str, float]:
    """Calculate percentage distribution across breakpoints."""
    distribution = {}
    total_width = max(breakpoints.values()) if breakpoints else 1920

    for name, width in breakpoints.items():
        distribution[name] = round((width / total_width) * 100, 2)

    return distribution


def generate_css_media_queries(breakpoints: Dict[str, int]) -> str:
    """Generate CSS media query structure."""
    lines = ["/* Mobile-First Media Queries */\n"]

    sorted_breakpoints = sorted(breakpoints.items(), key=lambda x: x[1])

    for i, (name, width) in enumerate(sorted_breakpoints):
        lines.append(f"/* {name.capitalize()} (>= {width}px) */")
        lines.append(f"@media (min-width: {width}px) {{")
        lines.append(f"  /* {name} styles */")
        lines.append(f"}}\n")

    return "\n".join(lines)


def generate_scss_variables(breakpoints: Dict[str, int]) -> str:
    """Generate SCSS variable structure."""
    lines = ["// Responsive Breakpoints\n"]

    for name, width in sorted(breakpoints.items(), key=lambda x: x[1]):
        var_name = "$breakpoint-" + name.replace(' ', '-').lower()
        lines.append(f"{var_name}: {width}px;")

    lines.append("\n// Mixin for media queries")
    lines.append("@mixin respond-to($breakpoint) {")
    lines.append("  @media (min-width: #{map-get($breakpoints, $breakpoint)}) {")
    lines.append("    @content;")
    lines.append("  }")
    lines.append("}\n")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Calculate optimal responsive design breakpoints"
    )
    parser.add_argument(
        "--preset",
        choices=list(DESIGN_SYSTEM_PRESETS.keys()),
        help="Use predefined breakpoint preset"
    )
    parser.add_argument(
        "--max-width",
        type=int,
        default=1920,
        help="Maximum viewport width to consider"
    )
    parser.add_argument(
        "--output-format",
        choices=["json", "css", "scss", "table", "all"],
        default="table",
        help="Output format"
    )

    args = parser.parse_args()

    if args.preset:
        breakpoints = DESIGN_SYSTEM_PRESETS[args.preset]
    else:
        breakpoints = generate_mobile_first_breakpoints(args.max_width)

    distribution = calculate_viewport_distribution(breakpoints)

    if args.output_format in ["json", "all"]:
        output = {
            "breakpoints": breakpoints,
            "distribution": distribution,
            "total_breakpoints": len(breakpoints)
        }
        print(json.dumps(output, indent=2))

    if args.output_format in ["css", "all"]:
        print(generate_css_media_queries(breakpoints))

    if args.output_format in ["scss", "all"]:
        print(generate_scss_variables(breakpoints))

    if args.output_format == "table":
        print("Responsive Breakpoints:")
        print("-" * 60)
        print(f"{'Breakpoint':<20} {'Width':<12} {'Distribution':<15}")
        print("-" * 60)

        for name, width in sorted(breakpoints.items(), key=lambda x: x[1]):
            pct = distribution[name]
            print(f"{name:<20} {width:<12}px {pct:>6}%")

        print("-" * 60)
        print(f"Total: {len(breakpoints)} breakpoints")


if __name__ == "__main__":
    main()
