<!-- v1.0 -->
## Flow control: loops, conditions, subflows

### repeat
Repeats a block of commands. Two forms:

**Fixed count** — when the test case gives an exact number of repetitions:
```yaml
- repeat:
    times: 5
    commands:
      - tapOn: "Add to cart"
```

**Conditional (`while`)** — repeats as long as a condition holds. Use `visible`/`notVisible`
for UI-state loops, or `true` with a JS expression for counter-based loops:
```yaml
- repeat:
    while:
      visible: "Update available"
    commands:
      - tapOn: "Dismiss"
      - assertNotVisible: "Dismiss"
```
```yaml
- evalScript: ${output.attempt = 0}
- repeat:
    while:
      true: ${output.attempt < 3}
    commands:
      - tapOn: "Refresh Data"
      - evalScript: ${output.attempt++}
```

### retry
Retries a block of commands on failure, up to a configured number of attempts —
use for flaky steps rather than as a substitute for a correct selector/wait.

```yaml
- retry:
    maxRetries: 3
    commands:
      - tapOn: "Submit"
      - assertVisible: "Success"
```

### runFlow (subflows)
Runs another flow file inline, or defines an inline subflow with `commands` — use to
reuse a common sequence (e.g. login) or to scope conditional logic.

```yaml
- runFlow: login.yaml
- runFlow:
    file: login.yaml
    env:
      USERNAME: testuser@example.com
```

Inline subflow (no separate file):
```yaml
- runFlow:
    label: "Sort alphabetically"
    commands:
      - tapOn: "Sort icon"
      - tapOn: "A-Z"
```

### Conditional execution (`when`)
`tapOn` and most action commands don't support conditions directly — wrap them in a
`runFlow` with a `when` block instead. All conditions inside a single `when` block
use AND logic.

Condition types:
| Key | True when |
|---|---|
| `visible: <selector>` | The matching element is visible |
| `notVisible: <selector>` | The matching element is not visible |
| `true: <JS expression>` | The expression evaluates to true / a non-empty value |
| `platform: Android \| iOS \| Web` | The current run platform matches |

```yaml
# Only tap "Allow" if the notification permission dialog appeared
- runFlow:
    when:
      visible: "Allow Notifications"
    commands:
      - tapOn: "Allow"

# Only run this branch on Android AND when the dialog is visible
- runFlow:
    when:
      platform: Android
      visible: "Allow Notifications"
    commands:
      - tapOn: "Allow"
```

Use this pattern whenever the test case describes optional/branching UI — e.g. "if a
permissions dialog appears, allow it" or "if onboarding is shown, skip it."