# Web Design Fundamentals

## Typography

### Font Selection

**Serif Fonts** (traditional, formal)
- Georgia, Times New Roman
- Best for: Long-form content, formal documents
- Screen-friendly serif: Georgia

**Sans-Serif Fonts** (modern, clean)
- Inter, Helvetica, Arial, Roboto, Open Sans
- Best for: UI, digital products, web
- Recommendation: Start with system fonts (Inter, Roboto)

**Monospace Fonts** (code, data)
- Courier New, Monaco, Fira Code
- Best for: Code blocks, data tables, technical content

### Font Pairing Strategy

**Good pairing:** One serif + one sans-serif

**Examples:**
- Georgia (serif) + Arial (sans-serif)
- Playfair Display (serif) + Inter (sans-serif)

**Or:** Two complementary sans-serif fonts

**Rule of thumb:**
- Heading: Larger, bolder
- Body: Smaller, lighter weight
- Monospace: For code and special content

### Type Scale

Maintain consistent ratios between font sizes.

**Modular Scale (1.25 multiplier):**
- Base: 16px
- Small: 13px (÷1.25)
- Large: 20px (×1.25)
- XL: 25px
- 2XL: 31px
- 3XL: 39px

**CSS Custom Properties:**
```css
:root {
  --font-size-base: 16px;
  --font-size-sm: 13px;
  --font-size-lg: 20px;
  --line-height-tight: 1.2;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.8;
}
```

### Line Height (Leading)
- **Headings:** 1.1 - 1.3 (tighter)
- **Body:** 1.5 - 1.8 (more spacious)
- **Code:** 1.4 - 1.6

### Letter Spacing (Tracking)
- **Normal:** 0 (default)
- **Headings:** Slightly negative (-0.02em) for tightness
- **Body:** Keep default
- **All caps:** Increase slightly (0.05em - 0.1em)

## Color Theory

### Color Models

**RGB (Web):** Red, Green, Blue (0-255 each)
- Used in: HTML, CSS, digital displays

**HSL (Designers):** Hue, Saturation, Lightness (0-100%)
- Easier to work with for variations
- Lightness: 50% = pure color, 0% = black, 100% = white

**Example:**
- Pure blue: `hsl(240, 100%, 50%)`
- Light blue: `hsl(240, 100%, 80%)`
- Dark blue: `hsl(240, 100%, 20%)`

### Color Psychology

**Red:** Energy, urgency, passion, warning
- CTA buttons, alerts, warnings

**Blue:** Trust, calm, professional, security
- Corporate, finance, healthcare

**Green:** Growth, success, health, nature
- Success messages, positive actions

**Yellow/Orange:** Warmth, optimism, caution
- Highlights, calls-to-action, warnings

**Purple:** Creativity, luxury, wisdom
- Premium products, creative fields

**Gray:** Neutral, professional, stable
- Backgrounds, disabled states, secondary text

### Color Contrast & Accessibility

**WCAG Standards:**
- **AA (minimum):** 4.5:1 for normal text, 3:1 for large text
- **AAA (enhanced):** 7:1 for normal text, 4.5:1 for large text

**Testing Tools:**
- WebAIM Contrast Checker
- Color Contrast Analyzer
- accessibility_auditor.py (included in this skill)

**Best Practices:**
- Pair dark text on light background (or vice versa)
- Avoid relying on color alone to convey meaning
- Test with colorblind-friendly palettes

## Layout & Spacing

### Spacing Scale

Consistent spacing creates visual rhythm and organization.

**8px Grid System (Recommended):**
- XS: 4px (tight spacing, icons)
- SM: 8px (small gaps between elements)
- MD: 16px (standard spacing)
- LG: 24px (section spacing)
- XL: 32px (major sections)
- 2XL: 48px (page sections)
- 3XL: 64px (layout breaks)

**CSS Implementation:**
```css
:root {
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
}
```

### Layout Systems

**CSS Grid (2D Layout):**
- Best for: Page layouts, card grids, complex structures
- Responsive: `grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))`

**Flexbox (1D Layout):**
- Best for: Navigation, toolbars, component layouts
- Responsive: `flex-wrap: wrap`, `gap: var(--spacing-md)`

### Common Breakpoints

| Name | Width | Use |
|------|-------|-----|
| Mobile | 320-480px | Small phones |
| Tablet | 481-1024px | Tablets, large phones |
| Desktop | 1025-1440px | Laptops, desktops |
| Wide | 1441px+ | Large monitors |

**Mobile-First Approach:**
```css
/* Mobile (default) */
.container { grid-template-columns: 1fr; }

/* Tablet and up */
@media (min-width: 768px) {
  .container { grid-template-columns: 1fr 1fr; }
}

/* Desktop and up */
@media (min-width: 1024px) {
  .container { grid-template-columns: repeat(3, 1fr); }
}
```

## Visual Hierarchy

### Sizing
- **Heading:** 28px - 48px
- **Subheading:** 20px - 28px
- **Body:** 14px - 16px
- **Caption:** 12px - 14px

### Weight
- **Heading:** Bold (700)
- **Subheading:** Semibold (600)
- **Body:** Normal (400)
- **Accent:** Bold (700) or Semibold (600)

### Color
- **Primary text:** Full saturation, high contrast
- **Secondary text:** Lighter color, lower contrast
- **Tertiary/disabled:** Gray, low contrast
- **Accent/CTA:** Bright, saturated color

## Whitespace

Whitespace (negative space) is as important as content.

**Benefits:**
- Reduces visual clutter
- Improves readability
- Creates focus
- Enhances elegance

**Principles:**
- Generous padding around content
- Breathing room between sections
- Smaller gaps within components
- Use whitespace to group related items

## Images & Media

### Image Optimization

**File Sizes:**
- Use modern formats (WebP, AVIF)
- Compress ruthlessly (tinypng.com, imageoptim.com)
- Serve responsive images (srcset, picture element)
- Lazy load below-the-fold images

**Best Practices:**
- Never stretch images
- Use object-fit for consistent sizing
- Provide alt text for all images
- Avoid text in images (accessibility)

### Image Ratios

- **16:9** (landscape): Videos, hero images
- **4:3** (standard): Photos, illustrations
- **1:1** (square): Avatars, thumbnails
- **3:2** (medium): Blog post headers

## Responsive Design

### Mobile-First Design

1. Start with mobile layout
2. Add features for larger screens
3. Test on actual devices

### Flexible Grids

```css
/* Fluid column width */
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));

/* Flex container */
flex-wrap: wrap;
flex: 1 1 300px;
```

### Responsive Typography

```css
/* Base: 16px on mobile */
body { font-size: 16px; }

/* 18px on tablet */
@media (min-width: 768px) {
  body { font-size: 18px; }
}

/* 20px on desktop */
@media (min-width: 1024px) {
  body { font-size: 20px; }
}
```

### Responsive Images

```html
<!-- Srcset for different densities -->
<img 
  src="image.jpg" 
  srcset="image.jpg 1x, image@2x.jpg 2x"
  alt="Description"
/>

<!-- Picture element for different layouts -->
<picture>
  <source media="(min-width: 1024px)" srcset="large.jpg">
  <source media="(min-width: 768px)" srcset="medium.jpg">
  <img src="small.jpg" alt="Description">
</picture>
```
