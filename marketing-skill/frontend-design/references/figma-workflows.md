# Figma Workflows & Best Practices

## File Organization

### Project Structure
```
Design System
├── 01_Foundations
│   ├── Colors
│   ├── Typography
│   ├── Icons
│   └── Spacing
├── 02_Components
│   ├── Button
│   ├── Input
│   ├── Card
│   └── Modal
├── 03_Patterns
│   ├── Forms
│   ├── Tables
│   ├── Navigation
│   └── Feedback
└── 04_Screens
    ├── Feature A
    ├── Feature B
    └── Feature C
```

### Page Organization Best Practices
- **One component per page** (or related variants)
- **Prefix pages with number:** 01_, 02_ (sorts naturally)
- **Use consistent naming:** Clear, searchable, hierarchical
- **Archive old pages:** Don't delete, just archive
- **Use "Assets" page:** Reusable shared elements

## Component Setup

### Component Variants (Recommended)
Instead of multiple components, use variants for states.

**Structure:**
```
Button
├── Component: Button
    ├── Size: Small, Medium, Large
    ├── Type: Primary, Secondary, Tertiary
    ├── State: Default, Hover, Active, Disabled
```

**Benefits:**
- Single source of truth
- Easier to maintain
- Auto-updates all instances
- Better for design tokens

### Component Properties
Document component properties in description:

```
Button / Primary / Medium / Default

Props:
- Label (required): Button text
- Size: Small (24px), Medium (32px), Large (40px)
- Type: Primary, Secondary, Tertiary
- State: Default, Hover, Active, Disabled
- Icon: Optional left/right icon
- Loading: Shows spinner, disables interaction

Spacing:
- Padding: 8px 16px (SM), 12px 24px (MD), 16px 32px (LG)
- Min width: 80px (avoid tiny buttons)

Accessibility:
- ARIA: Button semantic
- Focus: 2px offset outline
- Contrast: 4.5:1 minimum (AA)
```

## Design Tokens in Figma

### Using Design Tokens Plugin

1. **Install token plugin** (Tokens for Figma)
2. **Create token sets:**
   - Colors
   - Typography
   - Spacing
   - Border radius
   - Shadows

3. **Token structure:**
```
{
  "colors": {
    "primary": {
      "50": "#E3F2FD",
      "500": "#2196F3",
      "900": "#0D47A1"
    }
  },
  "spacing": {
    "xs": 4,
    "sm": 8,
    "md": 16,
    "lg": 24
  }
}
```

4. **Apply to components:**
   - Fill colors → token
   - Strokes → token
   - Text styles → token
   - Sizing → token

### Token Sync to Code
- Export to JSON
- Sync with CI/CD pipeline
- Generate CSS, JS, Tailwind configs
- Keep design and code in sync

## Design Specifications for Developers

### Preparing Specs

1. **Component Selection**
   - Select component in Figma
   - Right-click → Copy/Inspect

2. **Inspect Panel (Right Side)**
   - Dimensions (width, height)
   - Position (x, y)
   - Fill colors (HEX, RGB, opacity)
   - Stroke (color, width)
   - Typography (font, size, weight, line height)
   - Effects (shadows, blur)
   - Constraints (how it responds to resize)

3. **Create Handoff Document**
   - Screenshot or Figma link
   - Dimensions and spacing
   - Color values
   - Typography specifications
   - State variations
   - Responsive behavior

### Responsive Specifications

For each component, specify:

**Mobile (< 768px):**
- Dimensions
- Spacing
- Text size
- Layout changes

**Tablet (768px - 1024px):**
- Any layout changes
- Sizing updates

**Desktop (> 1024px):**
- Full-size specs

### Example Component Spec

```
Button

States: Default, Hover, Active, Disabled

Mobile (< 768px):
- Height: 40px
- Padding: 8px 16px
- Font: 14px, semibold
- Tap target: 44×44px minimum

Tablet (768px - 1024px):
- Height: 40px (same as mobile)
- Font: 14px (same as mobile)

Desktop (> 1024px):
- Height: 44px
- Padding: 12px 24px
- Font: 16px, semibold
- Cursor: pointer

All States:
- Primary: #2196F3 background, white text
- Hover: #1976D2 background
- Active: #1565C0 background
- Disabled: #BDBDBD background, #9E9E9E text

Focus State:
- Outline: 2px solid #2196F3
- Outline offset: 2px
```

## Collaboration Best Practices

### Team Permissions
- **Owner:** Can edit, manage access
- **Editor:** Can edit
- **Viewer:** Read-only
- **Comment only:** Can comment but not edit

### Review Process
1. **Designer creates component** in working file
2. **Request review** (add reviewers as comments)
3. **Reviewers provide feedback** (specific, actionable)
4. **Designer iterates** and updates
5. **Approve and merge** to main design system

### Version Control
- **Main file:** Source of truth
- **Working copies:** One per designer
- **Archive versions:** Keep old versions for reference
- **Naming:** Use dates or version numbers

### Communication
- Use Figma comments for design feedback
- Link to design specs in development tickets
- Update design system before implementation
- Keep handoff document updated

## Handoff Checklist

Before handing off to developers:

- [ ] All variants documented
- [ ] Dimensions specified (px, not vague)
- [ ] Colors as tokens or exact values (HEX)
- [ ] Typography specs complete (font, size, weight, line-height)
- [ ] Spacing consistent and documented
- [ ] Responsive behavior specified
- [ ] Focus/hover/active states included
- [ ] Accessibility notes (focus outline, contrast)
- [ ] Code examples provided (if applicable)
- [ ] Figma inspection panel accessible
- [ ] Design tokens exported to code
- [ ] All edge cases documented

## Advanced Workflows

### Auto-Layout for Responsive Design
- Set auto-layout on components
- Configure spacing, alignment, direction
- Components auto-reflow based on content
- Reduces manual resizing work

### Component Set Patterns
Create multiple components that work together:

```
Text Input
├── Text Input / Small
├── Text Input / Medium
├── Text Input / Large
└── Label (separate component)

Form Component
├── uses Text Input
├── uses Label
└── uses Help Text
```

### Design System Library
- Create shared library file
- Publish components to team
- Other files consume published components
- Updates propagate automatically

### Specs Export Tools
- **Zeplin:** Design handoff and specs
- **Avocode:** Design markup extraction
- **Figma plugins:** Design-to-code (HTML, React, etc.)

### Performance Tips
- Use components to reduce file size
- Archive old pages and versions
- Limit number of pages per file
- Use external libraries for shared assets
- Regularly clean up unused elements
