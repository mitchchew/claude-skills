#!/usr/bin/env python3
"""Analyze color palettes for harmony, contrast ratios, and accessibility compliance."""

import json
import argparse
import re
from typing import Tuple, List, Dict


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 6:
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    raise ValueError(f"Invalid hex color: {hex_color}")


def rgb_to_hsl(rgb: Tuple[int, int, int]) -> Tuple[float, float, float]:
    """Convert RGB to HSL."""
    r, g, b = [x / 255.0 for x in rgb]
    max_c = max(r, g, b)
    min_c = min(r, g, b)
    l = (max_c + min_c) / 2.0

    if max_c == min_c:
        h = s = 0.0
    else:
        d = max_c - min_c
        s = d / (2.0 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)

        if max_c == r:
            h = (g - b) / d + (6 if g < b else 0)
        elif max_c == g:
            h = (b - r) / d + 2
        else:
            h = (r - g) / d + 4
        h /= 6

    return h * 360, s * 100, l * 100


def calculate_relative_luminance(rgb: Tuple[int, int, int]) -> float:
    """Calculate relative luminance per WCAG spec."""
    r, g, b = [x / 255.0 for x in rgb]
    r = r / 12.92 if r <= 0.03928 else pow((r + 0.055) / 1.055, 2.4)
    g = g / 12.92 if g <= 0.03928 else pow((g + 0.055) / 1.055, 2.4)
    b = b / 12.92 if b <= 0.03928 else pow((b + 0.055) / 1.055, 2.4)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def calculate_contrast_ratio(rgb1: Tuple[int, int, int], rgb2: Tuple[int, int, int]) -> float:
    """Calculate contrast ratio between two colors."""
    l1 = calculate_relative_luminance(rgb1)
    l2 = calculate_relative_luminance(rgb2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def get_wcag_level(contrast: float) -> str:
    """Determine WCAG compliance level."""
    if contrast >= 7:
        return "AAA"
    elif contrast >= 4.5:
        return "AA"
    else:
        return "FAIL"


def analyze_palette(colors: List[str]) -> Dict:
    """Analyze a color palette for harmony and accessibility."""
    rgb_colors = []

    # Convert to RGB
    for color in colors:
        try:
            rgb = hex_to_rgb(color)
            rgb_colors.append((color, rgb))
        except ValueError:
            continue

    analysis = {
        "color_count": len(rgb_colors),
        "colors": [],
        "contrast_matrix": {},
        "accessibility": {
            "aa_pairs": 0,
            "aaa_pairs": 0,
            "total_pairs": 0
        }
    }

    # Analyze each color
    for hex_color, rgb in rgb_colors:
        hsl = rgb_to_hsl(rgb)
        analysis["colors"].append({
            "hex": hex_color,
            "rgb": f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})",
            "hsl": f"hsl({hsl[0]:.0f}, {hsl[1]:.0f}%, {hsl[2]:.0f}%)",
            "luminance": round(calculate_relative_luminance(rgb), 3)
        })

    # Analyze contrast between all color pairs
    for i, (hex1, rgb1) in enumerate(rgb_colors):
        for j, (hex2, rgb2) in enumerate(rgb_colors):
            if i < j:
                ratio = calculate_contrast_ratio(rgb1, rgb2)
                level = get_wcag_level(ratio)
                pair_key = f"{hex1} vs {hex2}"

                analysis["contrast_matrix"][pair_key] = {
                    "ratio": round(ratio, 2),
                    "wcag_level": level
                }

                analysis["accessibility"]["total_pairs"] += 1
                if level == "AA":
                    analysis["accessibility"]["aa_pairs"] += 1
                elif level == "AAA":
                    analysis["accessibility"]["aaa_pairs"] += 1

    return analysis


def generate_color_report(analysis: Dict) -> str:
    """Generate readable color analysis report."""
    lines = ["Color Palette Analysis Report\n"]
    lines.append(f"Total Colors: {analysis['color_count']}\n")

    lines.append("## Colors\n")
    for color in analysis["colors"]:
        lines.append(f"- {color['hex']}")
        lines.append(f"  RGB: {color['rgb']}")
        lines.append(f"  HSL: {color['hsl']}")
        lines.append(f"  Luminance: {color['luminance']}\n")

    lines.append("## Contrast Analysis\n")
    for pair, contrast_data in analysis["contrast_matrix"].items():
        level = contrast_data['wcag_level']
        ratio = contrast_data['ratio']
        status = "✓" if level != "FAIL" else "✗"
        lines.append(f"{status} {pair}: {ratio}:1 ({level})")

    lines.append(f"\n## Accessibility Summary\n")
    a11y = analysis["accessibility"]
    lines.append(f"Total Pairs: {a11y['total_pairs']}")
    lines.append(f"AA Compliant: {a11y['aa_pairs']}")
    lines.append(f"AAA Compliant: {a11y['aaa_pairs']}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Analyze color palettes for harmony and accessibility"
    )
    parser.add_argument(
        "--colors",
        type=str,
        nargs="+",
        help="List of hex colors to analyze"
    )
    parser.add_argument(
        "--input",
        type=str,
        help="JSON file with color palette definition"
    )
    parser.add_argument(
        "--output-format",
        choices=["text", "json"],
        default="text",
        help="Output format"
    )

    args = parser.parse_args()

    colors = []

    if args.input:
        try:
            with open(args.input) as f:
                data = json.load(f)
                if isinstance(data, dict):
                    colors = data.get("colors", [])
                elif isinstance(data, list):
                    colors = data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading input file: {e}")
            exit(1)

    if args.colors:
        colors.extend(args.colors)

    if not colors:
        print("Error: No colors provided")
        exit(1)

    analysis = analyze_palette(colors)

    if args.output_format == "json":
        print(json.dumps(analysis, indent=2))
    else:
        print(generate_color_report(analysis))


if __name__ == "__main__":
    main()
