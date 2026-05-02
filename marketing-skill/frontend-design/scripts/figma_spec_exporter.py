#!/usr/bin/env python3
"""Export component specifications from design data (for handoff to developers)."""

import json
import argparse
from pathlib import Path
from typing import Dict, Any, List


def generate_component_spec(component: Dict[str, Any]) -> str:
    """Generate markdown specification for a component."""
    lines = [
        f"# {component['name']}",
        f"\n**Type:** {component.get('type', 'Component')}",
        f"**Status:** {component.get('status', 'Draft')}",
    ]

    if component.get('description'):
        lines.append(f"\n## Description\n{component['description']}")

    if component.get('usage'):
        lines.append(f"\n## Usage\n{component['usage']}")

    # Variants
    if component.get('variants'):
        lines.append("\n## Variants\n")
        for variant in component['variants']:
            lines.append(f"- **{variant['name']}**: {variant.get('description', '')}")

    # Properties/States
    if component.get('properties'):
        lines.append("\n## Properties\n")
        lines.append("| Property | Type | Default | Description |")
        lines.append("|----------|------|---------|-------------|")
        for prop in component['properties']:
            lines.append(
                f"| {prop['name']} | {prop['type']} | {prop.get('default', '-')} | {prop.get('description', '')} |"
            )

    # Spacing
    if component.get('spacing'):
        lines.append("\n## Spacing\n")
        spacing = component['spacing']
        lines.append(f"- Padding: {spacing.get('padding', 'N/A')}")
        lines.append(f"- Margin: {spacing.get('margin', 'N/A')}")
        lines.append(f"- Gap: {spacing.get('gap', 'N/A')}")

    # Responsive
    if component.get('responsive'):
        lines.append("\n## Responsive Behavior\n")
        lines.append("| Breakpoint | Behavior |")
        lines.append("|------------|----------|")
        for bp, behavior in component['responsive'].items():
            lines.append(f"| {bp} | {behavior} |")

    # Accessibility
    if component.get('accessibility'):
        lines.append("\n## Accessibility\n")
        a11y = component['accessibility']
        lines.append(f"- **ARIA**: {a11y.get('aria', 'N/A')}")
        lines.append(f"- **Keyboard**: {a11y.get('keyboard', 'N/A')}")
        lines.append(f"- **Color Contrast**: {a11y.get('contrast', 'AA')}")

    # Code Example
    if component.get('code_example'):
        lines.append("\n## Code Example\n")
        lines.append("```jsx")
        lines.append(component['code_example'])
        lines.append("```")

    return "\n".join(lines)


def export_component_library(components: List[Dict[str, Any]], output_dir: str):
    """Export all component specifications to markdown files."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Generate index
    index_lines = ["# Component Library\n"]
    index_lines.append("## Components\n")

    for component in components:
        spec = generate_component_spec(component)
        filename = component['name'].lower().replace(' ', '-') + '.md'
        filepath = output_path / filename
        filepath.write_text(spec)

        index_lines.append(f"- [{component['name']}]({filename})")

    index_file = output_path / "README.md"
    index_file.write_text("\n".join(index_lines))

    return len(components)


def generate_design_token_css(tokens: Dict[str, Any]) -> str:
    """Generate CSS custom properties for design tokens."""
    lines = [":root {"]

    def flatten(obj: Dict, prefix: str = ""):
        for key, value in obj.items():
            if isinstance(value, dict):
                flatten(value, f"{prefix}{key}-")
            else:
                var_name = f"--{prefix}{key}".lower().replace('_', '-')
                lines.append(f"  {var_name}: {value};")

    flatten(tokens)
    lines.append("}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Export component specifications for design-to-code handoff"
    )
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Input JSON file with component definitions"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="./component-specs",
        help="Output directory for specifications"
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json", "all"],
        default="markdown",
        help="Output format"
    )

    args = parser.parse_args()

    try:
        with open(args.input) as f:
            data = json.load(f)

        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        if args.format in ["markdown", "all"]:
            components = data.get('components', [])
            count = export_component_library(components, str(output_dir))
            print(f"✓ Exported {count} components to {output_dir}")

        if args.format in ["json", "all"]:
            json_file = output_dir / "components.json"
            with open(json_file, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"✓ Generated {json_file}")

        if args.format in ["markdown", "all"] and data.get('design_tokens'):
            css_file = output_dir / "design-tokens.css"
            css_content = generate_design_token_css(data['design_tokens'])
            css_file.write_text(css_content)
            print(f"✓ Generated {css_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{args.input}' not found")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{args.input}'")
        exit(1)
    except KeyError as e:
        print(f"Error: Missing required field {e}")
        exit(1)


if __name__ == "__main__":
    main()
