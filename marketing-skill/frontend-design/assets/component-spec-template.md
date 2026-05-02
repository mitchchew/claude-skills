# Component Specification Template

Use this template to document a single component for development handoff.

---

# Component: [Component Name]

**Type:** [Atom/Molecule/Organism]
**Status:** [Draft/Ready/Production]
**Last Updated:** [Date]

## Overview

[1-2 sentence description of what this component does and when to use it]

### When to Use
- Use case 1
- Use case 2
- Use case 3

### When NOT to Use
- Avoid case 1
- Avoid case 2

---

## Visual Specification

### Anatomy

```
[Component structure diagram or description]

- Part 1: [Description]
- Part 2: [Description]
- Part 3: [Description]
```

### Dimensions

#### Mobile (< 640px)
- Height: [value]px
- Width: [full width / value]px
- Padding: [value]px
- Spacing from other elements: [value]px

#### Tablet (640px - 1024px)
- Height: [value]px
- Width: [value]px
- Padding: [value]px

#### Desktop (> 1024px)
- Height: [value]px
- Width: [value]px
- Padding: [value]px

---

## States & Variants

### Variants

| Variant | Description | Use When |
|---------|-------------|----------|
| [Name] | [Description] | [Usage] |
| [Name] | [Description] | [Usage] |

### States

#### Default
[Screenshot/description]
- Background: [color/value]
- Text: [color/value]
- Border: [color/value]
- Shadow: [value]

#### Hover
[Screenshot/description]
- Background: [color/value]
- Cursor: [pointer/default/text]
- Transition: [duration]ms [easing]

#### Active/Pressed
[Screenshot/description]
- Background: [color/value]
- Transform: [scale/translate]

#### Focus
[Screenshot/description]
- Outline: 2px solid [color]
- Outline Offset: 2px

#### Disabled
[Screenshot/description]
- Opacity: [value]%
- Cursor: not-allowed
- Pointer Events: none

#### Loading
[Screenshot/description]
- Shows: [spinner/skeleton/other]
- Text: [hidden/changed]
- Interaction: [disabled/unchanged]

---

## Colors

| Element | Color | Hex | Token | Contrast |
|---------|-------|-----|-------|----------|
| Background | [Name] | [#RRGGBB] | `--color-name` | [ratio]:[1] |
| Text | [Name] | [#RRGGBB] | `--color-name` | [ratio]:[1] |
| Border | [Name] | [#RRGGBB] | `--color-name` | N/A |
| Hover BG | [Name] | [#RRGGBB] | `--color-name` | [ratio]:[1] |

---

## Typography

### Text Content

| Element | Font Size | Font Weight | Line Height | Letter Spacing |
|---------|-----------|-------------|-------------|-----------------|
| Label | [size]px | [weight] | [value] | [value] |
| Value | [size]px | [weight] | [value] | [value] |

### Font Family

- Primary Font: [Font Name] (fallback: [fallback])
- Usage: [When to use]

---

## Spacing

### Internal Spacing (Padding)
```
[Visual representation or description]

- Top: [value]px
- Right: [value]px
- Bottom: [value]px
- Left: [value]px
```

### External Spacing (Margin)
- Above: [value]px
- Below: [value]px
- Left/Right: [value]px

### Gap Between Child Elements
- Horizontal: [value]px
- Vertical: [value]px

---

## Responsive Behavior

### Mobile Layout
[Description of how component adapts on mobile]

- Layout: [vertical/horizontal/other]
- Text size: Scales to [size]px
- Spacing: [adjusted values]
- Touch target minimum: 44px × 44px

### Tablet Layout
[Description of how component adapts on tablet]

### Desktop Layout
[Description of how component adapts on desktop]

---

## Accessibility

### Semantic HTML
- Element: `<[element]>`
- Role: [role]

### ARIA Attributes
- `aria-label`: "[Description]"
- `aria-describedby`: [id]
- `aria-disabled`: true/false
- Other: [list any other ARIA]

### Keyboard Interaction
| Key | Action |
|-----|--------|
| Tab | [behavior] |
| Shift+Tab | [behavior] |
| Enter | [behavior] |
| Space | [behavior] |
| Escape | [behavior] |

### Focus Management
- Focus indicator: Yes / No
- Focus outline: 2px solid [color]
- Outline offset: 2px

### Color Accessibility
- Contrast ratio: [ratio]:[1] (meets WCAG AA/AAA)
- Not color-only indication
- Colorblind friendly

---

## Code Example

### HTML
```html
<div class="component">
  <label for="input">Label</label>
  <input id="input" type="text" placeholder="Placeholder">
  <button>Action</button>
</div>
```

### CSS
```css
.component {
  padding: var(--spacing-md);
  background: var(--color-bg);
  border-radius: var(--radius-md);
}

.component input {
  padding: var(--spacing-sm);
  border: 1px solid var(--color-border);
  font-size: var(--font-size-base);
}

.component button {
  padding: var(--spacing-md) var(--spacing-lg);
  background: var(--color-primary);
  color: white;
  border-radius: var(--radius-md);
  cursor: pointer;
}

.component button:focus {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.component button:disabled {
  opacity: 50%;
  cursor: not-allowed;
}
```

### React
```jsx
export function Component({
  label,
  placeholder = "Enter text",
  disabled = false,
  onSubmit,
  loading = false,
  error = null
}) {
  const [value, setValue] = useState("");

  return (
    <div className="component">
      {label && <label htmlFor="input">{label}</label>}
      <input
        id="input"
        type="text"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        placeholder={placeholder}
        disabled={disabled || loading}
        aria-describedby={error ? "error-message" : undefined}
      />
      {error && <span id="error-message">{error}</span>}
      <button 
        onClick={() => onSubmit(value)}
        disabled={disabled || loading}
      >
        {loading ? "Loading..." : "Submit"}
      </button>
    </div>
  );
}
```

---

## Edge Cases

### Empty State
- Description: [How component appears with no content]
- Display: [Show placeholder / disable / hide]

### Error State
- Error message: [How displayed]
- Visual indicator: [Color, icon, border]
- Recovery: [How user fixes error]

### Loading State
- Show spinner
- Disable interactions
- Show skeleton (optional)

### Overflow Content
- Long text: [Truncate / wrap / scroll]
- Too many items: [Paginate / virtualize / show more]

---

## Performance Considerations

- Rendering: [Memoization needed? yes/no]
- Re-renders: [When does component re-render?]
- Lazy loading: [Load on demand? yes/no]
- Bundle impact: [Size in KB]

---

## Browser Support

- Chrome/Edge: Latest 2 versions
- Firefox: Latest 2 versions
- Safari: Latest 2 versions
- Mobile browsers: Latest versions

---

## Related Components

- [Related component 1](link)
- [Related component 2](link)
- [Component that uses this](link)

---

## Figma Link

**[Link to Figma component]**

---

## Questions & Feedback

[Contact information for design team]

---

**Approved By:** [Name]
**Approval Date:** [Date]
**Implementation Deadline:** [Date]
