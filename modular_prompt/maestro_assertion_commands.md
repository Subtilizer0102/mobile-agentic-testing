<!-- v1.0 -->
## Assertion commands

Commands that verify the app is in the expected state. Use these to encode the
"expected result" part of a test case, not just the actions.

### assertVisible
Asserts a UI element is visible on screen. Auto-retries for up to 7 seconds while
waiting for it to appear — you don't need manual waits before it for normal cases.

```yaml
- assertVisible: "Welcome back"
- assertVisible:
    text: "My Button"
    enabled: true
```

### assertNotVisible
Asserts a UI element is NOT present/visible on screen. Same selector options and
auto-retry behavior as `assertVisible`.

```yaml
- assertNotVisible: "Error message"
```

### assertTrue
Asserts that a JavaScript expression evaluates to true — for logic/state checks
that aren't simply "is this element visible" (e.g. comparing two captured values).

```yaml
- assertTrue: ${output.itemCount > 0}
```

### assertWithAI
Uses AI vision to verify complex UI states described in natural language, when a
simple element selector can't express the check (e.g. "the chart shows an upward
trend"). Defaults to `optional: true`.

```yaml
- assertWithAI:
    assertion: "The shopping cart icon shows a badge with a number greater than 0"
```

### assertNoDefectsWithAI
AI-powered visual scan of the current screen for UI defects/anomalies (overlapping
text, cut-off elements, broken layout) without specifying what to look for.

```yaml
- assertNoDefectsWithAI
```

### assertScreenshot
Visual regression test — compares the current screen against a previously saved
reference screenshot and fails if they differ beyond a threshold.

```yaml
- assertScreenshot: "home_screen_baseline"
```

### extractTextWithAI
Uses AI vision to extract structured text/data from the screen into a variable,
for cases where the value isn't cleanly exposed via the accessibility tree.

```yaml
- extractTextWithAI:
    query: "the total price shown on the checkout screen"
    outputVariable: totalPrice
```

### When to use which
- Prefer **`assertVisible`/`assertNotVisible`** for anything expressible as "this
  text/id is (not) on screen" — they're fast, deterministic, and don't need AI.
- Reach for the **`...WithAI`** commands only when the test case describes a
  visual/semantic condition that a plain selector genuinely can't capture.