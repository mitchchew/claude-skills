# Accessibility Standards (WCAG)

## Overview

**WCAG 2.1** (Web Content Accessibility Guidelines) is the standard for web accessibility.

### Conformance Levels

- **Level A (Minimum):** Lowest standard, basic accessibility
- **Level AA (Recommended):** Good accessibility, meets most user needs
- **Level AAA (Enhanced):** Highest standard, comprehensive accessibility

**Industry Standard:** Aim for **Level AA** as minimum.

## The 4 Principles (POUR)

### 1. Perceivable
Users must be able to perceive content.

**Guideline 1.1 - Text Alternatives**
- Every image needs alt text
- Alt text: Concise description of image content/purpose
- ❌ "image123.jpg"
- ✓ "Woman working at a desk with laptop"

**Guideline 1.3 - Adaptable**
- Content must be presentable without loss of meaning
- Use semantic HTML (headings, lists, labels)
- Don't rely on layout/appearance alone

**Guideline 1.4 - Distinguishable**
- Content must be easy to see and hear
- Contrast ratio: 4.5:1 for normal text (AA), 7:1 for AAA
- Don't use color alone to convey information
- Allow text resizing (avoid fixed font sizes in pixels)

### 2. Operable
Users must be able to navigate and interact.

**Guideline 2.1 - Keyboard Accessible**
- All functionality available via keyboard
- No keyboard traps (can't get out of an element)
- Tab order makes sense (logical, left-to-right)
- Visible focus indicators (don't remove default focus outline)

**Guideline 2.4 - Navigable**
- Clear purpose of each link/button
- Link text is descriptive (❌ "Click here", ✓ "Download PDF report")
- Consistent navigation patterns across site
- Skip links for main content

**Guideline 2.5 - Input Modalities**
- Support multiple input types (keyboard, pointer, voice)
- Touch targets minimum 44×44 pixels
- No sudden context changes on focus/input

### 3. Understandable
Users must understand the content.

**Guideline 3.1 - Readable**
- Clear, plain language
- Define unusual words or abbreviations
- Reading level appropriate for audience

**Guideline 3.2 - Predictable**
- Consistent navigation and layout
- Consistent identification of components
- No unexpected context changes

**Guideline 3.3 - Input Assistance**
- Labels for form fields (associated with `<label>`)
- Error messages clearly identify the problem
- Suggestions provided for error correction
- Form validation on submit, not necessarily on blur

### 4. Robust
Content must be compatible with assistive technologies.

**Guideline 4.1 - Compatible**
- Valid HTML (proper tag nesting, unique IDs)
- ARIA attributes used correctly
- Status messages announced to screen readers

## Common WCAG Violations

### Color Contrast Issues
❌ **Problem:** Gray text on white background fails WCAG AA
```
Text: #999999 on #FFFFFF = 4.1:1 ratio (Fails AA)
```

✓ **Solution:** Darker gray or darker background
```
Text: #666666 on #FFFFFF = 7:1 ratio (Passes AAA)
```

### Missing Form Labels
❌ **Problem:** Input without associated label
```html
<input type="email" placeholder="Email">
```

✓ **Solution:** Use `<label>` with `for` attribute
```html
<label for="email">Email Address</label>
<input id="email" type="email" required>
```

### Missing Alt Text
❌ **Problem:** Image without alt text
```html
<img src="hero.jpg">
```

✓ **Solution:** Descriptive alt text
```html
<img src="hero.jpg" alt="Team celebrating project launch">
```

### Missing Focus Indicators
❌ **Problem:** No visible focus outline
```css
button:focus { outline: none; }
```

✓ **Solution:** Keep or style the focus outline
```css
button:focus { outline: 2px solid #0066CC; outline-offset: 2px; }
```

### Color-Only Information
❌ **Problem:** Status only indicated by color
```
Red background = error
```

✓ **Solution:** Add text, icon, or other indicator
```
Red background + "✗ Error" text
```

## Testing Checklist

### Automated Testing
- [ ] Run accessibility scanner (WAVE, axe DevTools)
- [ ] Check color contrast (WebAIM Contrast Checker)
- [ ] Validate HTML (W3C HTML Validator)

### Keyboard Testing
- [ ] Navigate entire site with Tab key only
- [ ] Focus order is logical
- [ ] No keyboard traps
- [ ] Can activate all interactive elements
- [ ] Focus indicator is visible

### Screen Reader Testing
- [ ] Page structure makes sense (headings, landmarks)
- [ ] Form labels associated correctly
- [ ] Image alt text is descriptive
- [ ] Link text is meaningful
- [ ] Status messages announced

### Visual Testing
- [ ] Sufficient color contrast
- [ ] Text is resizable (up to 200%)
- [ ] No text in images (except decorative)
- [ ] Mobile-friendly (touch targets 44×44px minimum)

## Semantic HTML

Use correct HTML elements for their intended purpose.

### Document Structure
```html
<html lang="en">
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <header>
      <nav>Navigation</nav>
    </header>
    <main>
      <article>
        <h1>Article Title</h1>
        <section>...</section>
      </article>
      <aside>Sidebar</aside>
    </main>
    <footer>Footer</footer>
  </body>
</html>
```

### Heading Structure
```html
<h1>Main Page Title (one per page)</h1>
<h2>Section Heading</h2>
<h3>Subsection</h3>
<!-- Don't skip levels: h1 → h3 -->
```

### Forms
```html
<form>
  <label for="name">Full Name</label>
  <input id="name" type="text" required>
  
  <label for="email">Email</label>
  <input id="email" type="email" required>
  
  <button type="submit">Submit</button>
</form>
```

### Lists
```html
<!-- Ordered list -->
<ol>
  <li>First step</li>
  <li>Second step</li>
</ol>

<!-- Unordered list -->
<ul>
  <li>Item one</li>
  <li>Item two</li>
</ul>
```

## ARIA Attributes

Use ARIA only when semantic HTML isn't available.

### Common ARIA Attributes
- `aria-label`: Label for elements without visible text
- `aria-labelledby`: Links element to visible heading
- `aria-describedby`: Longer description
- `aria-hidden="true"`: Hide from screen readers
- `aria-live="polite"`: Announce changes to screen reader
- `aria-invalid="true"`: Mark invalid form fields
- `role="button"`: Make non-button element keyboard accessible

### Example
```html
<!-- Button with no visible text -->
<button aria-label="Close menu">✕</button>

<!-- Dynamic alert updates -->
<div aria-live="polite" aria-atomic="true">
  <p>Form submitted successfully</p>
</div>

<!-- Associate description with field -->
<input id="password" aria-describedby="pwd-hint">
<small id="pwd-hint">At least 8 characters, one uppercase</small>
```

## Tools & Resources

### Testing Tools
- **WebAIM Contrast Checker** — Color contrast testing
- **WAVE** — Browser extension for accessibility scanning
- **axe DevTools** — Automated accessibility testing
- **Lighthouse** — Chrome DevTools built-in accessibility audit
- **NVDA/JAWS** — Screen readers for testing
- **accessibility_auditor.py** — Included in this skill

### Validators
- **W3C HTML Validator** — HTML validation
- **WCAG 2.1 Level AA Checklist** — Quick reference
- **Accessibility Inspector** (Firefox) — Element inspection

### Learning Resources
- **WCAG 2.1 Guidelines** — https://www.w3.org/WAI/WCAG21/quickref/
- **WebAIM** — https://webaim.org/
- **A11y Project** — https://www.a11yproject.com/
