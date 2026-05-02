# Design System Template

Complete template for documenting a design system. Copy and customize for your project.

---

# [Your Company] Design System

**Version:** 1.0.0
**Last Updated:** [Date]
**Maintained By:** [Team]

## Overview

[1-2 sentence description of what this design system is and why it exists]

### Quick Links
- [Components](#components)
- [Design Tokens](#design-tokens)
- [Accessibility](#accessibility)
- [Figma Library](#figma-library)

---

## Design Tokens

### Colors

#### Primary Colors
| Name | Hex | CSS Variable | Usage |
|------|-----|--------------|-------|
| Primary | #0066CC | `--color-primary` | Main CTA, primary actions |
| Success | #2ECC71 | `--color-success` | Success states, positive actions |
| Warning | #F39C12 | `--color-warning` | Warnings, caution states |
| Error | #E74C3C | `--color-error` | Errors, destructive actions |

#### Neutral Colors
| Name | Hex | CSS Variable | Usage |
|------|-----|--------------|-------|
| Gray 50 | #F9FAFB | `--color-gray-50` | Light backgrounds |
| Gray 500 | #6B7280 | `--color-gray-500` | Secondary text |
| Gray 900 | #111827 | `--color-gray-900` | Primary text |

### Typography

#### Font Families
```css
--font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
--font-mono: 'Fira Code', monospace;
```

#### Font Sizes
| Name | Size | Usage |
|------|------|-------|
| xs | 12px | Captions, labels |
| sm | 14px | Body small, metadata |
| base | 16px | Body text |
| lg | 20px | Subheadings |
| xl | 24px | Headings |
| 2xl | 32px | Large headings |

#### Font Weights
- **Regular:** 400
- **Medium:** 500
- **Semibold:** 600
- **Bold:** 700

#### Line Heights
- **Tight:** 1.2
- **Normal:** 1.5
- **Relaxed:** 1.8

### Spacing Scale
```
--spacing-xs: 4px
--spacing-sm: 8px
--spacing-md: 16px
--spacing-lg: 24px
--spacing-xl: 32px
--spacing-2xl: 48px
--spacing-3xl: 64px
```

### Border Radius
```
--radius-sm: 4px
--radius-md: 8px
--radius-lg: 12px
--radius-full: 9999px
```

### Shadows
```
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
```

---

## Components

### Button

**Purpose:** Primary interaction element. Triggers action or navigation.

**Usage:**
- Primary actions (main CTA on page)
- Form submission
- Navigation between screens

**Variants:**

| Variant | Background | Text | Usage |
|---------|-----------|------|-------|
| Primary | `--color-primary` | White | Main actions |
| Secondary | `--color-gray-100` | `--color-gray-900` | Secondary actions |
| Tertiary | Transparent | `--color-primary` | Minimal, deemphasized |
| Danger | `--color-error` | White | Destructive actions |

**States:**
- Default
- Hover
- Active (pressed)
- Focus (outline)
- Disabled
- Loading (shows spinner)

**Sizes:**
- Small (32px height)
- Medium (40px height)
- Large (48px height)

**Spacing:**
- Padding: xs=8px 12px, md=12px 24px, lg=16px 32px
- Min width: 80px (to avoid tiny buttons)

**Accessibility:**
- Keyboard accessible (Tab, Enter/Space)
- Clear focus outline
- Loading state announced
- 4.5:1 color contrast minimum

**Code:**
```jsx
<Button variant="primary" size="medium" onClick={handleClick}>
  Click Me
</Button>
```

---

### Form Input

**Purpose:** User data entry field.

**Usage:**
- Text input
- Email validation
- Password entry
- Search queries

**Variants:**
- Text input
- Email input
- Password input
- Number input
- Date input

**States:**
- Default (empty)
- Focus (border highlight)
- Filled (with value)
- Error (red border, error message)
- Success (green border, checkmark)
- Disabled (grayed out)

**Spacing:**
- Padding: 8px 12px (medium)
- Height: 40px minimum (44px ideal for touch)
- Label above input
- 8px gap between label and input

**Accessibility:**
- Label associated with input (`for` attribute)
- Error message linked (`aria-describedby`)
- Help text available
- Clear focus indicator
- Semantic input types (email, password, etc.)

**Code:**
```jsx
<div>
  <label htmlFor="email">Email Address</label>
  <input 
    id="email" 
    type="email" 
    placeholder="you@example.com"
    aria-describedby="email-help"
  />
  <small id="email-help">We'll never share your email</small>
</div>
```

---

### Card

**Purpose:** Container for grouped content.

**Usage:**
- Product display
- Article preview
- User profile
- Statistics display

**Anatomy:**
- Image/media (optional)
- Header (title, subtitle)
- Body (content)
- Footer (actions, metadata)

**States:**
- Default
- Hover (lift effect, shadow increase)
- Active (border highlight)

**Spacing:**
- Padding: 16px-24px
- Gap between sections: 12px-16px

**Variants:**
- Elevated (shadow)
- Outlined (border)
- Flat (no shadow/border)

**Code:**
```jsx
<Card>
  <Card.Image src="..." alt="..." />
  <Card.Header title="Title" subtitle="Subtitle" />
  <Card.Body>Content here</Card.Body>
  <Card.Footer>
    <Button>Action</Button>
  </Card.Footer>
</Card>
```

---

## Layout & Responsive Design

### Breakpoints

| Name | Width | Usage |
|------|-------|-------|
| Mobile | < 640px | Phones |
| Tablet | 640px - 1024px | Tablets |
| Desktop | > 1024px | Laptops, desktops |

### Grid System

**12-column grid**
- Gutter: 16px (mobile), 24px (desktop)
- Column width: responsive
- Max width: 1200px

### Spacing Rules

- **Within component:** Use `--spacing-xs` or `--spacing-sm`
- **Between sections:** Use `--spacing-md` or `--spacing-lg`
- **Major layout:** Use `--spacing-xl` or `--spacing-2xl`

---

## Accessibility (WCAG AA)

### Color Contrast

Minimum 4.5:1 for normal text, 3:1 for large text.

**Tool:** WebAIM Contrast Checker

### Keyboard Navigation

- All interactive elements keyboard accessible
- Logical tab order
- Visible focus indicators
- No keyboard traps

### Semantic HTML

- Use `<button>` for buttons
- Use `<nav>` for navigation
- Use `<h1>`-`<h6>` for headings
- Use `<label>` for form fields

### ARIA

- `aria-label` for icon-only buttons
- `aria-labelledby` for headings
- `aria-describedby` for descriptions
- `aria-live` for dynamic updates

---

## Figma Library

**[Link to Figma file]**

### How to Use

1. Open Figma project
2. Right-click component
3. Select "Drag to create copy" or use copy/paste
4. Customize as needed

### Component Naming

All components prefixed with "Component /" for easy searching.

**Example:** Component / Button / Primary / Medium

---

## Implementation Guide

### CSS Custom Properties

```css
/* Use these variables instead of hardcoded values */
button {
  background-color: var(--color-primary);
  padding: var(--spacing-md) var(--spacing-lg);
  font-family: var(--font-sans);
  border-radius: var(--radius-md);
}
```

### Installing Design System

```bash
npm install @company/design-system
```

### Usage Example

```jsx
import { Button, Input, Card } from '@company/design-system';

export function MyComponent() {
  return (
    <Card>
      <h1>Title</h1>
      <Input label="Name" />
      <Button>Submit</Button>
    </Card>
  );
}
```

---

## Contributing

### Adding a New Component

1. Design in Figma
2. Create component page: `03_Components > [ComponentName]`
3. Document specs (size, spacing, states)
4. Code component (HTML/CSS/React)
5. Add to library
6. Document in this guide
7. Get approval from design system team

### Versioning

- Major: Breaking changes
- Minor: New features
- Patch: Bug fixes

---

## Support & Questions

- **Slack:** #design-system
- **Email:** design-team@company.com
- **Docs:** [Link to full documentation]

---

**Last Updated:** [Date]
**Next Review:** [Date 6 months out]
