#!/usr/bin/env python3
"""Audit design and code for WCAG accessibility compliance."""

import json
import argparse
import re
from pathlib import Path
from typing import Dict, List, Tuple


def calculate_contrast_ratio(rgb1: Tuple[int, int, int], rgb2: Tuple[int, int, int]) -> float:
    """Calculate WCAG contrast ratio between two RGB colors."""
    def relative_luminance(rgb: Tuple[int, int, int]) -> float:
        r, g, b = [x / 255.0 for x in rgb]
        r = r / 12.92 if r <= 0.03928 else pow((r + 0.055) / 1.055, 2.4)
        g = g / 12.92 if g <= 0.03928 else pow((g + 0.055) / 1.055, 2.4)
        b = b / 12.92 if b <= 0.03928 else pow((b + 0.055) / 1.055, 2.4)
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    l1 = relative_luminance(rgb1)
    l2 = relative_luminance(rgb2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def parse_rgb_color(color: str) -> Tuple[int, int, int] | None:
    """Parse RGB color from string."""
    rgb_match = re.match(r'rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', color)
    if rgb_match:
        return tuple(int(x) for x in rgb_match.groups())

    hex_match = re.match(r'#([0-9a-f]{6})', color.lower())
    if hex_match:
        hex_str = hex_match.group(1)
        return (
            int(hex_str[0:2], 16),
            int(hex_str[2:4], 16),
            int(hex_str[4:6], 16)
        )
    return None


def check_contrast_wcag(contrast: float) -> str:
    """Determine WCAG level for contrast ratio."""
    if contrast >= 7:
        return "AAA"
    elif contrast >= 4.5:
        return "AA"
    else:
        return "FAIL"


def audit_html_file(filepath: str) -> Dict:
    """Audit HTML file for accessibility issues."""
    issues = {
        "missing_alt_text": [],
        "missing_lang_attr": False,
        "missing_title": False,
        "missing_form_labels": [],
        "empty_headings": [],
        "heading_skip": [],
        "link_text": []
    }

    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    # Check for lang attribute
    if not re.search(r'<html[^>]*\slang=', content):
        issues["missing_lang_attr"] = True

    # Check for title
    if not re.search(r'<title>', content):
        issues["missing_title"] = True

    # Check for alt text on images
    img_matches = re.finditer(r'<img[^>]*>', content)
    for match in img_matches:
        if not re.search(r'\salt=', match.group()):
            issues["missing_alt_text"].append(match.group())

    # Check for form labels
    input_matches = re.finditer(r'<input[^>]*id=["\']([^"\']+)["\'][^>]*>', content)
    for match in input_matches:
        input_id = match.group(1)
        if not re.search(rf'<label[^>]*for=["\']{input_id}["\']', content):
            issues["missing_form_labels"].append(input_id)

    # Check for empty headings
    heading_matches = re.finditer(r'<h([1-6])>\s*</h\1>', content)
    for match in heading_matches:
        issues["empty_headings"].append(f"<h{match.group(1)}>")

    # Check for heading hierarchy
    headings = re.findall(r'<h([1-6])', content)
    prev_level = 0
    for heading_level in [int(h) for h in headings]:
        if heading_level > prev_level + 1:
            issues["heading_skip"].append(
                f"Jump from H{prev_level} to H{heading_level}"
            )
        prev_level = heading_level

    # Check for empty links
    link_matches = re.finditer(r'<a[^>]*>\s*</a>', content)
    for match in link_matches:
        issues["link_text"].append(match.group())

    return issues


def main():
    parser = argparse.ArgumentParser(
        description="Audit design and code for WCAG accessibility compliance"
    )
    parser.add_argument(
        "--check-contrast",
        type=str,
        nargs=2,
        metavar=("FOREGROUND", "BACKGROUND"),
        help="Check contrast ratio between two colors (hex or rgb)"
    )
    parser.add_argument(
        "--audit-html",
        type=str,
        help="Audit HTML file for accessibility issues"
    )
    parser.add_argument(
        "--output-format",
        choices=["text", "json"],
        default="text",
        help="Output format"
    )

    args = parser.parse_args()

    results = {}

    if args.check_contrast:
        fg = parse_rgb_color(args.check_contrast[0])
        bg = parse_rgb_color(args.check_contrast[1])

        if not fg or not bg:
            print("Error: Could not parse colors. Use hex (#RRGGBB) or rgb(R,G,B)")
            exit(1)

        ratio = calculate_contrast_ratio(fg, bg)
        level = check_contrast_wcag(ratio)
        results["contrast"] = {
            "ratio": round(ratio, 2),
            "wcag_level": level,
            "passes_aa": level in ["AA", "AAA"],
            "passes_aaa": level == "AAA"
        }

    if args.audit_html:
        if not Path(args.audit_html).exists():
            print(f"Error: File '{args.audit_html}' not found")
            exit(1)

        issues = audit_html_file(args.audit_html)
        results["html_audit"] = {
            "file": args.audit_html,
            "issues": issues,
            "issue_count": sum(len(v) if isinstance(v, list) else (1 if v else 0)
                             for v in issues.values())
        }

    if args.output_format == "json":
        print(json.dumps(results, indent=2))
    else:
        if "contrast" in results:
            c = results["contrast"]
            print(f"Contrast Ratio: {c['ratio']}:1")
            print(f"WCAG Level: {c['wcag_level']}")
            print(f"Passes AA: {'✓' if c['passes_aa'] else '✗'}")
            print(f"Passes AAA: {'✓' if c['passes_aaa'] else '✗'}\n")

        if "html_audit" in results:
            audit = results["html_audit"]
            print(f"HTML Audit: {audit['file']}")
            print(f"Total Issues: {audit['issue_count']}\n")
            for key, value in audit['issues'].items():
                if value and isinstance(value, list):
                    print(f"  {key}: {len(value)} found")
                elif value:
                    print(f"  {key}: ✗")


if __name__ == "__main__":
    main()
