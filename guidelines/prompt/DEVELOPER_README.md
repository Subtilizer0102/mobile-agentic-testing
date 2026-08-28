# Example Rules for Domain-Agnostic UI Agents

## Purpose

Examples strongly shape agent behavior. They should teach general interaction patterns, not scripts tied to specific websites or domains.

> **Goal:** Examples should help the agent decide what to do based on the current visible UI state.

---

## 1. Core Principle

Teach interaction patterns, not website types.

- ❌ *“On a shopping site, click Add to Cart.”*
- ✅ *“When a panel is already open, interact with its visible options instead of reopening it.”*

Examples must generalize across unknown interfaces.

---

## 2. Patterns Examples Should Cover

Use 8–16 short, atomic examples per prompt. Each example should demonstrate one behavior.

### State-Based Decisions
Actions should depend on the current UI state.
- **Control closed** → open it.
- **Control already open** → interact with its options.
- **Control already enabled** → continue.
- **Error visible** → correct the relevant input.

### Trigger vs. Sub-Action
Clearly distinguish between opening a control and operating inside it.
- **Selector closed** → open selector.
- **Selector open** → choose an option; do not reopen it.

### Reactive UI
When an action changes the UI, respond to the new state.
- **Action causes a menu to appear** → interact with the visible menu.
- **Dialog appears** → operate inside the dialog.
- **Section expands** → use the newly revealed controls.

### Minimal Forward Action
Choose the smallest action that advances the task.
- **Target off-screen** → scroll.
- **Target visible** → interact with it.
- **Options visible** → select the appropriate option.

*Avoid redundant or exploratory actions when the target state is already clear.*

### Error Recovery
React to visible validation or error states.
- **Required field is empty** → provide the missing input.
- **Invalid value is flagged** → correct that value.
- **Error message identifies a specific field** → fix that field rather than repeating the previous action.

### Element Disambiguation
Distinguish between similar elements using visible structure.

Use:
- Position
- Grouping
- Nearby labels
- Associated text
- Container relationships

*Avoid ambiguous references when multiple similar elements exist.*

### Visibility-Driven Navigation
Base navigation on what is currently visible.
- **Control not visible** → scroll or switch the relevant view.
- **Control becomes visible** → interact with it.

### Confirmation State
Recognize when the requested action has already completed.
- **Confirmation or success state visible** → do not repeat the triggering action.

### Blocked-by-Human Steps
Recognize when progress requires human input or approval.
- **Human confirmation required** → stop and wait rather than repeatedly attempting the action.

### Suggestions / Autocomplete
Treat dynamically displayed suggestions as the active UI.
- **Suggestions appear** → choose from the visible suggestions.
- **No suggestions visible** → continue with the appropriate available interaction.

### Existing Toggle State
Avoid changing a control unnecessarily.
- **Toggle already enabled** → leave it enabled.
- **Toggle disabled** → enable it when appropriate.

### Already-Visible Dialogs
Operate within an existing dialog.
- **Dialog already visible** → interact with its controls.
- **Do not trigger the action** that would reopen the dialog.

---

## 3. What Examples Must Avoid

### No Domain-Specific Sites or Brands
Avoid examples involving:
- Shopping
- Booking
- Banking
- Social media
- Named platforms or websites

*The behavior should remain domain-neutral.*

### No Vertical Vocabulary
Avoid domain-specific terms such as:
- Product, Cart, Checkout
- Post, Like, Share
- Hotel, Flight, Booking, Order, Payment

Prefer neutral terms:
- Item, Entry, Record
- Option, Selector, Input
- Primary action, Panel, Dialog

### No Long Multi-Step Stories
Avoid scripted journeys:
`Step 1 → Step 2 → Step 3 → Step 4`

Prefer atomic situations:
`Visible UI condition → correct next interaction`

### No Fixed Value Habits
Do not repeatedly use the same:
- Names
- Dates
- Quantities
- Search terms
- Values

*Use varied, neutral placeholders when values are necessary.*

### No Widget Over-Specialization
Do not fill the example set with variations of the same widget type.

Maintain coverage across:
- Controls
- Dialogs
- Panels
- Inputs
- Toggles
- Suggestions
- Validation states
- Visibility changes

### No Hidden Intent Assumptions
Examples should react to visible UI state, not assumed user goals.

*Avoid examples that implicitly assume the user wants to purchase, share, book, submit, or perform any particular domain action.*

---

## 4. Recommended Example Format

Keep each example to three parts:

> `Visible condition` → `UI change, if any` → `correct next interaction`

#### **Good**
> *Selector is expanded and options are visible* → *choose an option.*

#### **Bad**
> *Size dropdown is open on a clothing page* → *select Medium.*

*The first teaches a reusable interaction pattern. The second teaches a domain-specific script.*

---

## 5. Example Quality Checklist

Before adding an example, verify:

- [ ] It teaches one interaction pattern.
- [ ] It depends on visible UI state.
- [ ] It is domain-agnostic.
- [ ] It uses neutral UI vocabulary.
- [ ] It avoids a fixed action sequence.
- [ ] It demonstrates the smallest useful next action.
- [ ] It does not assume hidden user intent.
- [ ] It does not duplicate another example unnecessarily.
- [ ] The overall example set covers diverse UI states.

---

## 6. Target Coverage

Across the full example set, cover:

- [ ] Already-open vs. closed controls
- [ ] Reactive UI changes
- [ ] Validation errors
- [ ] Duplicate or similar elements
- [ ] Off-screen targets
- [ ] Confirmation states
- [ ] Human-blocked steps
- [ ] Suggestions / autocomplete
- [ ] Already-set toggles
- [ ] Already-visible dialogs

> **Design Principle:** Prefer pattern diversity over multiple examples of the same pattern in different domains.