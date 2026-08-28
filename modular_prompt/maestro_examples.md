## Interaction pattern examples

These examples teach **reusable interaction patterns**, not scripts for any
specific app or domain. Each one shows: a visible UI condition → what changes (if
anything) → the correct Maestro command(s) to issue next.

When generating a flow, apply the *pattern*, not the literal element names shown
here — substitute in whatever text, id, or structure the actual test case
describes. Do not copy these element names into unrelated flows.

---

### 1. Closed control → open it
**Situation:** A collapsible control (dropdown, expandable section, selector) is
closed and its options are not visible.
**Correct interaction:** Tap the control to open it.
```yaml
- tapOn: "Category Selector"
```

### 2. Open control → choose from it, don't reopen
**Situation:** A control is already open and its options are visible.
**Correct interaction:** Tap the desired option directly. Do not tap the control
again — that would close it instead of selecting anything.
```yaml
- tapOn: "Option B"
```

### 3. Action reveals a new panel → operate within it
**Situation:** Tapping a control causes a new panel, menu, or dialog to appear.
**UI change:** A dialog labeled "New Record" is now visible with its own inputs.
**Correct interaction:** Interact with the newly revealed panel's controls next —
don't repeat the action that opened it.
```yaml
- tapOn: "Add"
- assertVisible: "New Record"
- tapOn: "Title"
- inputText: "Draft Entry One"
```

### 4. Section expands → use the newly revealed controls
**Situation:** Tapping a header or toggle expands a collapsed section, revealing
additional controls that weren't there before.
**Correct interaction:** Interact with the specific control now revealed inside
the expanded section, not the header again.
```yaml
- tapOn: "Advanced Settings"
- tapOn: "Sync Frequency"
```

### 5. Validation error → correct the specific flagged field
**Situation:** After submitting, an error message identifies a particular input as
invalid.
**Correct interaction:** Fix that specific field. Do not repeat the submit action
that triggered the error — it will fail again with the same input still wrong.
```yaml
- assertVisible: "Enter a value between 1 and 100"
- tapOn: "Quantity"
- eraseText: 5
- inputText: "42"
```

### 6. Required field empty → provide the missing input
**Situation:** A required input is currently empty (no error shown yet, but the
next action depends on it being filled).
**Correct interaction:** Fill the field before proceeding to the next step.
```yaml
- tapOn: "Label"
- inputText: "Sample Value B"
```

### 7. Similar/duplicate elements → disambiguate with structure, not guesswork
**Situation:** Multiple elements share the same visible text (e.g. several rows
each have a "Remove" control).
**Correct interaction:** Anchor the selector to a nearby stable label, container,
or position rather than assuming the first match is correct.
```yaml
- tapOn:
    text: "Remove"
    below: "Entry Alpha"
```

### 8. Target off-screen → scroll toward it, then act
**Situation:** The element the next step needs to interact with isn't currently
visible on screen.
**UI change:** Scrolling brings it into view.
**Correct interaction:** Scroll until the target is visible before attempting to
tap it — don't attempt the tap first.
```yaml
- scrollUntilVisible:
    element:
      text: "Configuration Panel"
    direction: DOWN
- tapOn: "Configuration Panel"
```

### 9. Target already visible → act directly, skip unnecessary scrolling
**Situation:** The element the next step needs is already visible on the current
screen.
**Correct interaction:** Interact with it immediately. Adding a scroll or extra
navigation step here would be a redundant, non-minimal action.
```yaml
- tapOn: "Primary Action"
```

### 10. Control not visible on current view → switch view, then interact
**Situation:** The needed control doesn't exist on the currently displayed
screen/tab/view at all (not just off-screen — it's on a different view).
**Correct interaction:** Navigate to the correct view first, then interact with
the control once it becomes visible.
```yaml
- tapOn: "Filters Tab"
- assertVisible: "Sort Order"
- tapOn: "Sort Order"
```

### 11. Confirmation/success already visible → don't repeat the triggering action
**Situation:** A success or confirmation state is already visible, indicating the
prior action already completed.
**Correct interaction:** Verify the confirmation state; do not re-issue the action
that produced it.
```yaml
- assertVisible: "Changes saved"
```

### 12. Step requires external/human confirmation → wait, don't fabricate
**Situation:** Progressing depends on input that isn't available within the app's
own UI (e.g. a code delivered externally, manual approval from another person or
system).
**Correct interaction:** Wait for the resulting UI state rather than guessing or
inventing a value that was never provided in the test case.
```yaml
- extendedWaitUntil:
    visible: "Verified"
    timeout: 30000
```

### 13. Suggestions appear → select from the visible list
**Situation:** Typing into an input causes a list of suggestions/autocomplete
results to appear.
**Correct interaction:** Treat the suggestion list as the active UI and select
from it, rather than continuing to type past it.
```yaml
- tapOn: "Search Input"
- inputText: "Sample Query"
- tapOn: "Suggested Result 1"
```

### 14. No suggestions appear → proceed with the entered value as-is
**Situation:** After typing into an input, no suggestion list appears.
**Correct interaction:** Continue the flow using the value already entered — don't
wait for or attempt to trigger suggestions that aren't there.
```yaml
- tapOn: "Search Input"
- inputText: "Sample Query"
- pressKey: enter
```

### 15. Toggle already in the desired state → leave it, don't tap it
**Situation:** A toggle/switch/checkbox is already enabled (or already matches the
state the test case wants).
**Correct interaction:** Verify the state; do not tap it, since tapping would flip
it to the *wrong* state.
```yaml
- assertVisible:
    id: "auto_sync_toggle"
    checked: true
```

### 16. Already-visible dialog → operate inside it, don't retrigger the opener
**Situation:** A dialog or panel is already open on screen (e.g. it appeared from
a previous step, or was open at flow start).
**Correct interaction:** Interact with the dialog's own controls directly. Do not
tap the button that originally opens the dialog — doing so risks closing it or
having no effect, since it's already open.
```yaml
- assertVisible: "Filter Options"
- tapOn: "Apply"
```