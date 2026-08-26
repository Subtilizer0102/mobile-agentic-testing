<!-- v1.0 -->
## Maestro flow file structure

A Maestro flow file has two parts, separated by a line containing only `---`:

1. **Header** (YAML front matter) — config for the flow.
2. **Command list** — a YAML array of commands, executed top to bottom.

```yaml
appId: com.example.app
---
- launchApp
- tapOn: "Login"
```

### Header fields

| Field | Purpose |
|---|---|
| `appId` | Required for native apps. Android package name or iOS bundle ID. Can be a regex to match app ID variants across build flavors. |
| `url` | Use instead of `appId` when testing a website in a mobile browser. |
| `name` | Optional display name for the flow. |
| `tags` | Optional list of tags used to filter which flows run (e.g. `tags: [smoke, login]`). |
| `onFlowStart` | Optional list of commands to run before the flow starts (setup). |
| `onFlowComplete` | Optional list of commands to run after the flow finishes, pass or fail (teardown). |
| `androidWebViewHierarchy: devtools` | Add when testing an Android WebView screen that Maestro's default accessibility hierarchy can't read. |

### Command list rules

- Each item is either a **bare string** for commands with no parameters:
```yaml
  - launchApp
  - back
  - hideKeyboard
```
  or a **map** with the command name as the key:
```yaml
  - tapOn: "Continue"
  - inputText: "hello@example.com"
```
- Comments start with `#` and are ignored by the parser.
- Every command supports two optional universal arguments:
  - `optional: true` — if the command fails, the flow keeps running instead of stopping (default: `false`, except AI-powered commands which default to `true`).
  - `label: "..."` — a human-readable description shown in test output/logs instead of the raw command. Also useful for hiding sensitive literal values (like passwords) from logs.

```yaml
  - tapOn:
      id: "buy_now_button"
      label: "Tap on Buy Now button"
  - inputText:
      text: "mySecr3tPassw0rd!"
      label: "Enter the test user's password"
  - assertVisible:
      text: "Summer sale is here!"
      optional: true
```

### Environment variables and parameters

You can declare variables in the header and reference them in commands with `${VAR_NAME}`:

```yaml
appId: com.example.app
env:
  USERNAME: testuser@example.com
  PASSWORD: Test1234!
---
- launchApp
- tapOn: "Email"
- inputText: ${USERNAME}
- tapOn: "Password"
- inputText: ${PASSWORD}
```

If the natural-language test case doesn't specify literal values (e.g. "log in with valid
credentials"), use clearly-named placeholder values or `env` variables rather than
guessing real-looking data.