# Frontend Design Skill

Comprehensive frontend design expertise covering UI/UX design, web design, design systems, accessibility, component design, and design-to-code workflows.

## Quick Start

1. **Read the main skill:** [SKILL.md](SKILL.md)
2. **Review reference materials:** [references/](references/)
3. **Use asset templates:** [assets/](assets/)
4. **Run Python tools:** [scripts/](scripts/)

## What's Inside

### SKILL.md
Master documentation with:
- Core competencies
- Workflow framework
- Engagement patterns
- Quick reference guide

### References
Expert knowledge bases:
- `design-systems.md` — Design system setup, component libraries, design tokens
- `ui-ux-principles.md` — Information architecture, user flows, interaction design
- `web-design-fundamentals.md` — Typography, color theory, layout, responsive design
- `accessibility-standards.md` — WCAG guidelines, testing, inclusive design
- `figma-workflows.md` — Figma best practices, design handoff, specifications
- `component-design-patterns.md` — Atomic design, component composition, patterns

### Scripts
Python CLI tools (no external dependencies):
- `design_token_generator.py` — Generate CSS custom properties and design tokens
- `accessibility_auditor.py` — Check color contrast, validate HTML, WCAG compliance
- `figma_spec_exporter.py` — Export component specifications for development
- `responsive_breakpoint_calculator.py` — Calculate optimal responsive breakpoints
- `color_palette_analyzer.py` — Analyze color harmony and accessibility

### Assets
Ready-to-use templates:
- `design-system-template.md` — Complete design system documentation template
- `component-spec-template.md` — Component specification for handoff
- `accessibility-checklist.md` — WCAG Level AA audit checklist
- `design-token-schema.json` — Design token structure template

## Common Workflows

### Design System Audit
→ Use `design-systems.md` reference
→ Run `accessibility_auditor.py` on current design
→ Document with `design-system-template.md`

### Figma Handoff
→ Read `figma-workflows.md`
→ Use `figma_spec_exporter.py` to generate specs
→ Use `component-spec-template.md` for documentation

### Accessibility Remediation
→ Use `accessibility-checklist.md`
→ Run `accessibility_auditor.py` to find issues
→ Reference `accessibility-standards.md` for solutions
→ Run `color_palette_analyzer.py` for color contrast

### Component Design
→ Review `component-design-patterns.md`
→ Create spec with `component-spec-template.md`
→ Reference `web-design-fundamentals.md` for styling
→ Test accessibility with `accessibility-checklist.md`

## Using Python Tools

### Installation
No external dependencies required. Run with:
```bash
python scripts/design_token_generator.py --help
python scripts/accessibility_auditor.py --help
python scripts/color_palette_analyzer.py --help
```

### Examples

**Generate CSS tokens:**
```bash
python scripts/design_token_generator.py \
  --input tokens.json \
  --output-format all \
  --output-dir dist/
```

**Check color contrast:**
```bash
python scripts/accessibility_auditor.py \
  --check-contrast "#2196F3" "#FFFFFF"
```

**Analyze color palette:**
```bash
python scripts/color_palette_analyzer.py \
  --colors "#2196F3" "#4CAF50" "#FF9800" \
  --output-format text
```

**Export responsive breakpoints:**
```bash
python scripts/responsive_breakpoint_calculator.py \
  --preset tailwind \
  --output-format json
```

## Quick Reference

### WCAG Accessibility Levels
- **AA (Recommended):** 4.5:1 color contrast, keyboard accessible, semantic HTML
- **AAA (Enhanced):** 7:1 color contrast, advanced accessibility features

### Responsive Breakpoints
- Mobile: < 640px
- Tablet: 640px - 1024px
- Desktop: > 1024px
- Wide: > 1440px

### Design Token Categories
- Colors (primary, secondary, success, warning, error, neutral)
- Typography (fonts, sizes, weights, line heights)
- Spacing (xs, sm, md, lg, xl, 2xl, 3xl)
- Border radius (sm, md, lg, xl, full)
- Shadows (sm, md, lg, xl, 2xl)

### Component States
- Default
- Hover
- Active
- Focus
- Disabled
- Loading

## Engagement Patterns

When the user mentions:
- **"I need a design system"** → Use design-systems.md + design-system-template.md
- **"Audit accessibility"** → Use accessibility-checklist.md + accessibility_auditor.py
- **"Set up Figma"** → Use figma-workflows.md + figma_spec_exporter.py
- **"Design a component"** → Use component-design-patterns.md + component-spec-template.md
- **"Improve consistency"** → Use design-systems.md + design-token-generator.py

## Support

For questions about:
- **Design systems:** See `design-systems.md`
- **Accessibility:** See `accessibility-standards.md`
- **Figma workflows:** See `figma-workflows.md`
- **Component patterns:** See `component-design-patterns.md`
- **Color accessibility:** Run `color_palette_analyzer.py`

---

**Version:** 1.0.0
**Last Updated:** May 2, 2026
**Status:** Production Ready
