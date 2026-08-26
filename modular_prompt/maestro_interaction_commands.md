<!-- v1.0 -->
## Interaction commands

Commands that simulate a user touching, typing into, or navigating the app.

### tapOn
Performs a tap gesture. The single most common command — use for buttons, links,
list items, icons, checkboxes, etc.

Parameters: `selector` (string shorthand or map), `point`, `repeat` (int, tap N times),
`delay` (ms between repeats, default 100), `retryTapIfNoChange` (bool — retry the tap
if the UI didn't change, useful when the target wasn't ready yet), `waitToSettleTimeoutMs`.

```yaml
- tapOn: "Login"
- tapOn:
    id: "plus_button"
    repeat: 5
    delay: 200
- tapOn:
    point: "50%,50%"        # center of screen
```

### doubleTapOn / longPressOn
Same selector/parameter options as `tapOn`. `doubleTapOn` performs a double tap
(e.g. to like a post, zoom an image). `longPressOn` performs a long press (e.g. to
open a context menu or start a drag).

```yaml
- doubleTapOn: "Photo"
- longPressOn: "Message bubble"
```

### inputText
Types a text string into whatever field currently has keyboard focus. **You must
`tapOn` the field first** to focus it, unless it's already focused by default.

```yaml
- tapOn: "First name"
- inputText: "Test_first_name"
```

Related random-data variants: `inputRandomText`, `inputRandomNumber`,
`inputRandomEmail`, `inputRandomPersonName` (each accepts an optional `length:`).
Use these when the test case says something like "enter any valid text/number"
rather than a specific value.

### eraseText
Deletes characters from the currently focused field by simulating backspace.

```yaml
- eraseText              # removes up to 50 characters (default)
- eraseText: 10          # removes exactly 10 characters (max 100)
```

For long text, it's faster to select-all then erase:
```yaml
- longPressOn: "input_field_id"
- tapOn: "Select All"
- eraseText: 1
```

### copyTextFrom / pasteText
`copyTextFrom` reads the text of a matched element into the built-in
`${maestro.copiedText}` variable. `pasteText` pastes the current clipboard content
into the focused field.

```yaml
- copyTextFrom:
    id: "confirmation_code"
- tapOn: "Code field"
- pasteText
```

### swipe
Simulates a swipe gesture. Define it by `direction`, by `start`/`end` coordinates,
or starting `from` a specific element.

Parameters: `direction` (`LEFT`/`RIGHT`/`UP`/`DOWN`; cannot combine with start/end),
`start`, `end` (coordinates, relative % or absolute px), `from` (selector to start
the swipe at that element's center, optionally with a nested `point`),
`duration` (ms — higher = slower swipe, default 400), `waitToSettleTimeoutMs`.

```yaml
- swipe:
    direction: LEFT
- swipe:
    start: "90%,50%"
    end: "10%,50%"
- swipe:
    direction: UP
    duration: 800
```

### scroll
A simple vertical scroll down the screen — no parameters. Use for a single scroll
step; use `scrollUntilVisible` when you need to scroll until a specific element appears.

```yaml
- scroll
```

### scrollUntilVisible
Scrolls repeatedly in a direction until the target element becomes visible, or fails
on timeout.

Parameters: `element` (required selector), `direction` (`DOWN`/`UP`/`LEFT`/`RIGHT`,
default `DOWN`), `timeout` (ms, default 20000), `speed` (0–100, default 40),
`visibilityPercentage` (0–100, default 100), `centerElement` (bool, scroll until the
element is also away from the viewport edge).

```yaml
- scrollUntilVisible:
    element:
      text: "Terms and Conditions"
    direction: DOWN
    timeout: 15000
```

### pressKey
Presses a hardware/virtual key. One key per command.

Valid keys: `home`, `lock`, `enter`, `backspace`, `volume up`, `volume down`,
`back` (Android only), `power` (Android only), `tab` (Android only), plus
Android TV remote keys.

```yaml
- pressKey: home
- pressKey: enter
- pressKey: back
```

### back
Shorthand for the system back navigation gesture/button (equivalent to `pressKey: back`
but cross-platform — works the same way conceptually on iOS swipe-back too).

```yaml
- back
```

### hideKeyboard
Dismisses the on-screen keyboard if visible.

```yaml
- hideKeyboard
```

### openLink
Opens a URL or deep link, either in the app (if it handles that link) or the
system browser.

Parameters: `link` (required), `autoVerify` (bool — bypass Android's app-picker
disambiguation dialog / Chrome first-run agreement), `browser` (bool — force opening
in the web browser instead of the app).

```yaml
- openLink: "https://example.com"
- openLink:
    link: "myapp://profile/42"
    autoVerify: true
```