# Component Design Patterns

## Atomic Design Methodology

Structure components from smallest to largest:

### Atoms
Smallest, indivisible components. Building blocks.

**Examples:**
- Button
- Input field
- Label
- Icon
- Badge
- Tag

### Molecules
Simple combinations of atoms. Small functional units.

**Examples:**
- Form field (label + input + help text)
- Button with icon
- Search box (input + button)
- Card header (image + title)
- Navigation item (icon + text)

### Organisms
Complex combinations of molecules. Distinct sections.

**Examples:**
- Header (logo + nav + search)
- Form (multiple fields, validation, submit)
- Card (image + title + description + actions)
- Footer (links + copyright + social)
- Table (header + rows + pagination)

### Templates
Page-level structures. Combine organisms.

**Examples:**
- Landing page template
- Product list template
- Detail page template
- Dashboard template

### Pages
Specific instances of templates with real content.

**Examples:**
- Home page
- Product page
- User dashboard

## Component State Management

Every component needs defined states:

### Button States
```
Default → Hover → Active → Focus → Disabled → Loading
```

**Specifications:**
- **Default:** Initial appearance
- **Hover:** User hovers over element
- **Active/Pressed:** Currently being clicked or selected
- **Focus:** Keyboard focus indicator
- **Disabled:** Cannot interact (opacity, gray color, cursor)
- **Loading:** Shows spinner, disables interaction

### Form Input States
```
Default → Focus → Filled → Error → Success → Disabled
```

**Specifications:**
- **Default:** Empty, neutral appearance
- **Focus:** Border highlight, cursor visible
- **Filled:** User has entered value
- **Error:** Red border/text, error message
- **Success:** Green checkmark, success message
- **Disabled:** Grayed out, non-interactive

### Feedback States
```
Idle → Loading → Success → Error → Warning → Info
```

## Component Composition Patterns

### Compound Components
Components that work together but control internal state.

**Use case:** Tab component with Tab.List and Tab.Panel

```jsx
<Tabs defaultValue="tab1">
  <Tabs.List>
    <Tabs.Trigger value="tab1">Tab 1</Tabs.Trigger>
    <Tabs.Trigger value="tab2">Tab 2</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="tab1">Content 1</Tabs.Content>
  <Tabs.Content value="tab2">Content 2</Tabs.Content>
</Tabs>
```

**Benefits:**
- Flexible composition
- Shared state management
- Easy to customize

### Container/Presentational Pattern
Separate logic from UI.

```jsx
// Container (logic)
function UserListContainer() {
  const [users, setUsers] = useState([]);
  
  useEffect(() => {
    fetchUsers().then(setUsers);
  }, []);
  
  return <UserList users={users} />;
}

// Presentational (UI only)
function UserList({ users }) {
  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

**Benefits:**
- Reusable UI components
- Easy to test presentation
- Separation of concerns

### Render Props Pattern
Component passes state/logic to render function.

```jsx
<DataFetcher url="/api/users">
  {(data, loading, error) => (
    loading ? <Spinner /> :
    error ? <Error message={error} /> :
    <UserList users={data} />
  )}
</DataFetcher>
```

**Benefits:**
- Share logic without wrapper hell
- Maximum flexibility
- Child decides how to render

## Common Component Patterns

### Modal/Dialog
```
Dialog
├── Overlay (click to close)
├── Content
│   ├── Header (title, close button)
│   ├── Body (main content)
│   └── Footer (actions)
└── Focus trap (keep focus inside)
```

**Key behaviors:**
- Escape key closes
- Focus trapped inside
- Backdrop click closes (optional)
- Scrolling prevented behind modal

### Dropdown/Select
```
Trigger (button or input)
└── Popover
    └── Menu items
        ├── Text
        ├── Icon
        └── Badge
```

**Key behaviors:**
- Opens on click
- Closes on escape or click outside
- Keyboard navigation (arrow keys)
- Single selection by default

### Tooltip
```
Trigger (hover or focus)
└── Tooltip
    ├── Position (auto, top, bottom, left, right)
    ├── Content
    └── Arrow (optional)
```

**Key behaviors:**
- Shows on hover/focus
- Hides on blur/leave
- Auto-positioning to stay in viewport
- Accessible description

### Accordion
```
Accordion
├── Item
│   ├── Trigger (button)
│   └── Content (collapsed/expanded)
├── Item
│   ├── Trigger (button)
│   └── Content (collapsed/expanded)
```

**Key behaviors:**
- One item open at a time (optional)
- Smooth expand/collapse animation
- Accessible keyboard navigation
- Semantic heading structure

### Tabs
```
Tabs
├── TabList (role=tablist)
│   ├── Tab (role=tab, aria-selected=true/false)
│   ├── Tab
│   └── Tab
└── TabPanels
    ├── TabPanel (role=tabpanel)
    ├── TabPanel
    └── TabPanel
```

**Key behaviors:**
- Arrow keys navigate tabs
- Only active tab in focus order
- Content linked to tab (aria-labelledby)

## Design System Component Examples

### Button Component

**Anatomy:**
- Wrapper (interactive region)
- Label (text content)
- Icon (optional)
- Loading spinner (optional)

**Variants:**
- **Type:** primary, secondary, tertiary, danger
- **Size:** small (32px), medium (40px), large (48px)
- **State:** default, hover, active, focus, disabled, loading
- **Icon:** left, right, icon-only

**Code example:**
```jsx
<Button 
  variant="primary" 
  size="medium" 
  icon="arrow-right"
  loading={isSubmitting}
>
  Submit Form
</Button>
```

### Input Component

**Anatomy:**
- Label (associated with input)
- Input element
- Placeholder text
- Help text (optional)
- Error message (optional)
- Character counter (optional)

**Variants:**
- **Type:** text, email, password, number, date, etc.
- **Size:** small, medium, large
- **State:** default, focus, filled, error, success, disabled

**Code example:**
```jsx
<Input
  label="Email Address"
  type="email"
  placeholder="you@example.com"
  error="Invalid email format"
  helpText="We'll never share your email"
  required
/>
```

### Card Component

**Anatomy:**
- Container
- Image/media (optional)
- Header
  - Title
  - Subtitle
- Body (content)
- Footer
  - Actions
  - Metadata

**Variants:**
- **Elevation:** flat, raised, outlined
- **Interactive:** clickable, hoverable
- **Layout:** horizontal, vertical, compact

**Code example:**
```jsx
<Card 
  image={<img src="..." />}
  title="Product Name"
  description="Short description"
  footer={<Button>Learn More</Button>}
/>
```

## Responsive Component Behavior

### Mobile-First Progression

**Mobile Layout:**
- Single column
- Full width
- Stacked elements
- Larger touch targets (44×44px)

**Tablet Layout:**
- Two column
- Partial widths
- Better spacing
- Same touch targets

**Desktop Layout:**
- Multi-column
- Smaller elements
- Compact spacing
- Pointer-friendly sizes (can be smaller)

### Responsive Patterns

**Stacked → Grid:**
Mobile: Stack vertically
Desktop: Grid layout

**Hidden Elements:**
Mobile: Hide non-essential elements
Tablet/Desktop: Show all elements

**Navigation:**
Mobile: Hamburger menu
Tablet: Horizontal nav
Desktop: Full nav with dropdowns

**Tables:**
Mobile: Card/list view
Tablet: Scrollable table
Desktop: Full table

## Accessibility in Components

### Semantic HTML
- Use `<button>` for buttons, not `<div>`
- Use `<nav>` for navigation
- Use `<label>` for form fields
- Use `<h1>`-`<h6>` for headings

### ARIA Labels
- `aria-label` for icon-only buttons
- `aria-labelledby` to link heading to content
- `aria-describedby` for additional description
- `aria-live` for dynamic updates
- `role="button"` if using div as button

### Keyboard Navigation
- **Tab:** Move between focusable elements
- **Shift+Tab:** Move backward
- **Enter/Space:** Activate buttons
- **Arrow keys:** Navigate lists, tabs, menus
- **Escape:** Close modals, dropdowns

### Focus Management
- Always show focus indicator
- Logical tab order
- Focus trap in modals
- Return focus when closing modal

## Testing Components

### Visual Testing
- Screenshots at different breakpoints
- Color contrast validation
- Keyboard navigation
- Screen reader testing

### Interaction Testing
- All variants display correctly
- State changes work as expected
- Responsive behavior functions
- Accessibility features work

### Code Testing
- Unit tests for logic
- Accessibility tests (jest-axe)
- Integration tests for composition
- Visual regression tests

### User Testing
- Can users understand purpose?
- Do they interact as expected?
- Is feedback clear?
- Any accessibility issues?
