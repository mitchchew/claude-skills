# Accessibility (WCAG 2.1 Level AA) Checklist

Use this checklist before shipping any frontend design or code.

---

## Pre-Launch Audit

### Design Phase

#### Color & Contrast
- [ ] All text has at least 4.5:1 contrast ratio (AA standard)
- [ ] Large text (18px+) has at least 3:1 contrast ratio
- [ ] Focus states have visible 2px outline with 2:1 contrast
- [ ] Information is not conveyed by color alone (use icons/text too)
- [ ] Color palette is colorblind-friendly
- [ ] Tool used: WebAIM Contrast Checker or similar

#### Typography
- [ ] Minimum font size is 12px (readable on all devices)
- [ ] Line height is at least 1.4 (readable)
- [ ] Letter spacing is not less than -0.02em
- [ ] Text is not all caps (harder to read)
- [ ] Font weights are sufficient (not less than 300)

#### Layout & Spacing
- [ ] Touch targets are at least 44×44 pixels (mobile)
- [ ] Clickable elements have clear hover/focus states
- [ ] Elements are not too crowded (adequate whitespace)
- [ ] Responsive design works at 200% zoom
- [ ] Text can be resized to 200% without loss of functionality

#### Images & Icons
- [ ] Every image has descriptive alt text
- [ ] Decorative images have empty alt text (`alt=""`)
- [ ] Icons have labels or ARIA labels
- [ ] SVG icons have `role="img"` and `aria-label`

#### Forms
- [ ] All form fields have visible labels
- [ ] Labels are associated with inputs (`<label for="id">`)
- [ ] Required fields are marked
- [ ] Error messages are clear and specific
- [ ] Form validation occurs on submit (not real-time)
- [ ] Placeholder text is not the only label

---

### Development Phase

#### HTML Structure
- [ ] Page has single `<h1>` tag
- [ ] Heading hierarchy is correct (h1 → h2 → h3, no skipping)
- [ ] List content uses `<ul>`, `<ol>`, `<li>` tags
- [ ] Navigation uses `<nav>` element
- [ ] Main content uses `<main>` element
- [ ] Footers use `<footer>` element
- [ ] No empty headings
- [ ] Table has `<thead>`, `<tbody>`, `<th>` with `scope` attribute

#### Keyboard Navigation
- [ ] Entire page is navigable with Tab key
- [ ] Tab order is logical (left-to-right, top-to-bottom)
- [ ] No keyboard traps (can always get out)
- [ ] Skip to main content link present
- [ ] Focus is visible on all interactive elements (2px outline minimum)
- [ ] Focus outline has sufficient contrast (2:1 minimum)

#### ARIA & Semantic Elements
- [ ] Buttons use `<button>` element (not `<div>`)
- [ ] Links use `<a>` element (not `<span>`)
- [ ] Form controls use appropriate input types
- [ ] `aria-label` used for icon-only buttons
- [ ] `aria-labelledby` used to associate headings with content
- [ ] `aria-describedby` used for detailed descriptions
- [ ] `aria-hidden="true"` used on decorative elements
- [ ] `aria-live="polite"` used for dynamic updates
- [ ] No unnecessary `role` attributes
- [ ] ARIA attributes are correct and not conflicting

#### Images & Alt Text
- [ ] Every `<img>` has alt text
- [ ] Alt text is descriptive (not "image" or "photo")
- [ ] Alt text is concise (under 125 characters)
- [ ] Decorative images have empty alt (`alt=""`)
- [ ] Complex images have longer descriptions nearby
- [ ] SVGs have text content or title/desc elements

#### Forms & Validation
- [ ] All form fields are labeled
- [ ] Labels are properly associated (`<label for="id">`)
- [ ] Error messages linked to fields (`aria-describedby`)
- [ ] Error messages identify the problem and solution
- [ ] Form can be submitted without error
- [ ] Success message is announced to screen readers

#### Color & Contrast (Code)
- [ ] Text color contrast ≥ 4.5:1 (normal text)
- [ ] Large text contrast ≥ 3:1 (18px+ or 14px+ bold)
- [ ] UI component borders/outlines have ≥ 3:1 contrast
- [ ] Focus indicators have ≥ 3:1 contrast
- [ ] Tested with: axe DevTools, Lighthouse, WAVE

#### Responsive & Zoom
- [ ] Page is usable at 200% zoom
- [ ] No horizontal scrolling at 320px width
- [ ] Text is resizable without loss of content
- [ ] Text and images scale appropriately
- [ ] Functionality works on all tested breakpoints

---

### Testing Phase

#### Automated Testing
- [ ] WAVE browser extension run (0 errors, < 10 warnings)
- [ ] axe DevTools run (0 violations)
- [ ] Lighthouse accessibility score ≥ 90
- [ ] No red items in DevTools accessibility audit
- [ ] HTML validated with W3C Validator

#### Manual Keyboard Testing
- [ ] Navigate site with Tab key only (no mouse)
- [ ] Tab order is logical
- [ ] Focus visible on all elements
- [ ] Can activate all buttons and links
- [ ] Can fill all form fields
- [ ] Can close modals with Escape key
- [ ] Skip links work (if present)

#### Screen Reader Testing (NVDA, JAWS, or VoiceOver)
- [ ] Page structure makes sense (headings, landmarks)
- [ ] Images described properly
- [ ] Forms labeled clearly
- [ ] Buttons purpose clear
- [ ] Status messages announced
- [ ] Modals announced as dialogs
- [ ] Links distinguished from text
- [ ] Tables have proper headers

#### Visual & Color Testing
- [ ] All text readable (no low contrast)
- [ ] Focus outlines visible on all elements
- [ ] Color not only indicator (icons/text present)
- [ ] Tested with color blindness simulator (Sim Daltonism)
- [ ] Works with browser's dark mode

#### Mobile Accessibility
- [ ] Touch targets ≥ 44×44 pixels
- [ ] Tap targets have adequate spacing
- [ ] Double-tap zoom not required
- [ ] Screen magnification works (iOS/Android)
- [ ] Text resize works
- [ ] Works in landscape and portrait orientations

---

### Component Checklist

#### Buttons
- [ ] Text clearly states action
- [ ] 44×44px minimum touch target
- [ ] Has visible focus indicator
- [ ] Loading state announced
- [ ] Disabled state clear (not color-only)
- [ ] Tooltip if needed

#### Links
- [ ] Text describes destination
- [ ] Not "click here" or "read more"
- [ ] Underlined or otherwise visually distinct
- [ ] Focus outline visible
- [ ] Skip links included (if needed)

#### Form Fields
- [ ] Associated `<label>`
- [ ] Placeholder not sole label
- [ ] Required indicated clearly
- [ ] Error message linked
- [ ] Help text provided
- [ ] Auto-complete appropriate

#### Images
- [ ] Descriptive alt text
- [ ] Not text-in-image
- [ ] Linked images explain destination
- [ ] Icon images have labels

#### Modals
- [ ] Focus trapped inside
- [ ] Escape closes modal
- [ ] Focus returned to trigger
- [ ] Backdrop click closes (optional)
- [ ] Announced as dialog
- [ ] Can be dismissed

#### Dropdowns/Menus
- [ ] Arrow keys navigate
- [ ] Home/End keys work
- [ ] Escape closes menu
- [ ] Current item indicated
- [ ] Accessible name provided

#### Tables
- [ ] Row/column headers identified
- [ ] `<th scope="col/row">`
- [ ] Caption provided (if needed)
- [ ] Can be navigated with keyboard
- [ ] Not used for layout

#### Navigation
- [ ] Current page indicated
- [ ] Logical structure
- [ ] Consistent across pages
- [ ] Skip link to main content
- [ ] All items keyboard accessible

---

## Device Testing

### Screen Readers
- [ ] NVDA (Windows, free)
- [ ] JAWS (Windows, paid)
- [ ] VoiceOver (Mac/iOS, free)
- [ ] TalkBack (Android, free)

### Browser Testing
- [ ] Chrome + Chrome DevTools
- [ ] Firefox + Firefox DevTools
- [ ] Safari + Safari DevTools
- [ ] Edge + Edge DevTools

### Zoom & Magnification
- [ ] Zoom to 200%
- [ ] Zoom to 400%
- [ ] Browser magnification (Cmd/Ctrl +)
- [ ] OS magnification (Zoom on Mac, Magnifier on Windows)

### Color Vision Deficiency
- [ ] Protanopia (red-blind)
- [ ] Deuteranopia (green-blind)
- [ ] Tritanopia (blue-blind)
- [ ] Tools: Coblis, Color Blindness Simulator

---

## Common Issues & Fixes

### Issue: Low Color Contrast
**Fix:** Use darker color or lighter background
```
Bad:  Gray text (#999) on white = 4.1:1
Good: Gray text (#666) on white = 7:1
```

### Issue: Missing Form Label
**Fix:** Add associated `<label>` tag
```html
<!-- Bad -->
<input type="email" placeholder="Email">

<!-- Good -->
<label for="email">Email</label>
<input id="email" type="email">
```

### Issue: No Focus Outline
**Fix:** Style focus state clearly
```css
/* Good */
button:focus {
  outline: 2px solid blue;
  outline-offset: 2px;
}
```

### Issue: Image Without Alt Text
**Fix:** Add descriptive alt text
```html
<!-- Bad -->
<img src="team.jpg">

<!-- Good -->
<img src="team.jpg" alt="Engineering team at company retreat">
```

### Issue: Color-Only Information
**Fix:** Add text or icon
```html
<!-- Bad -->
<div style="background: red">Error</div>

<!-- Good -->
<div style="background: red">
  ✗ Error: Email is required
</div>
```

---

## Resources

### Testing Tools
- **WebAIM Contrast Checker** — https://webaim.org/resources/contrastchecker/
- **WAVE** — https://wave.webaim.org/
- **axe DevTools** — https://www.deque.com/axe/devtools/
- **Lighthouse** — Built into Chrome DevTools
- **WCAG 2.1 Checklist** — https://www.w3.org/WAI/WCAG21/quickref/

### Learning
- **WCAG 2.1 Guide** — https://www.w3.org/WAI/WCAG21/quickref/
- **MDN Web Docs** — https://developer.mozilla.org/en-US/docs/Web/Accessibility
- **Web Accessibility by WebAIM** — https://webaim.org/

---

## Audit Schedule

- **During Development:** Daily (developer responsibility)
- **Before Code Review:** Automated + manual keyboard test
- **Before QA:** Full accessibility audit
- **Before Launch:** Complete audit + screen reader test

---

## Sign-Off

- [ ] Accessibility audit completed
- [ ] All WCAG AA criteria met
- [ ] Screen reader tested
- [ ] Keyboard navigation tested
- [ ] Color contrast verified

**Audited By:** __________________ **Date:** __________

**Approved By:** __________________ **Date:** __________

---

**Last Updated:** [Date]
**WCAG Standard:** 2.1 Level AA
