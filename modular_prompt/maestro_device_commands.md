<!-- v1.0 -->
## App lifecycle & device commands

### launchApp
Launches the app under test. By default, stops the app first if it's already
running (fresh launch). If used with no `appId`, launches the app defined by the
flow's top-level `appId`.

Parameters: `appId` (optional override), `clearState` (bool — wipe app data before
launch, i.e. simulate a fresh install), `clearKeychain` (bool, iOS only — wipe the
entire iOS Keychain), `stopApp` (bool, default `true` — set `false` to bring an
already-running app to the foreground without restarting it), `permissions` (map of
permission name → `allow`/`deny`/`unset`; default is all permissions allowed),
`arguments` (map of launch arguments to pass into the app).

```yaml
- launchApp                                    # simplest form
- launchApp:
    clearState: true                            # fresh-install simulation
- launchApp:
    permissions:
      camera: allow
      location: deny
- launchApp:
    stopApp: false                              # foreground without restart
```

### killApp / stopApp
`killApp` force-stops the app and can optionally clear its data/cache. `stopApp`
stops the running app without clearing any state (use when a test needs to verify
behavior after backgrounding/re-launching).

```yaml
- stopApp
- killApp
```

### clearState
Clears app data, cache, and preferences to reset to a fresh-install state —
equivalent to `launchApp: { clearState: true }` but usable standalone, without
also launching.

```yaml
- clearState                 # clears the app under test
- clearState: com.other.app  # clears an arbitrary other app
```

### clearKeychain
iOS only — clears the entire iOS Keychain (affects all apps' stored credentials,
not just the one under test).

```yaml
- clearKeychain
```

### setPermissions
Grants/denies/unsets app permissions mid-flow (i.e. not just at launch time) — use
this before triggering a flow that isn't preceded by `launchApp`, such as opening a
deep link.

```yaml
- setPermissions:
    permissions:
      notifications: allow
      location: deny
```

### setLocation
Sets the simulated device GPS location.

```yaml
- setLocation:
    latitude: 37.7749
    longitude: -122.4194
```

### setOrientation
Changes device orientation.

```yaml
- setOrientation: LANDSCAPE_LEFT
- setOrientation: PORTRAIT
```

### setAirplaneMode / toggleAirplaneMode
`setAirplaneMode` sets airplane mode to an explicit on/off state; `toggleAirplaneMode`
flips whatever the current state is. Use to test offline behavior.

```yaml
- setAirplaneMode: enabled
- toggleAirplaneMode
```

### travel
Simulates time travel by adjusting the device's system clock — useful for testing
date-dependent features (subscriptions expiring, daily streaks, etc.).

```yaml
- travel:
    date: "2026-12-25"
```

### setClipboard
Sets the device clipboard to a specific text value (pairs with `pasteText`).

```yaml
- setClipboard: "promo-code-123"
- tapOn: "Promo code field"
- pasteText
```

### addMedia
Adds images or videos to the device's media gallery — use before testing a media
picker/upload flow.

```yaml
- addMedia:
    - "./test_files/sample_photo.jpg"
```

### takeScreenshot
Captures a screenshot and saves it to the test output directory. Good for
documenting a specific point in a flow.

```yaml
- takeScreenshot: "after_checkout"
```

### startRecording / stopRecording
Starts/stops a full screen recording of the run and saves it as a video file.

```yaml
- startRecording: "signup_flow"
- ...
- stopRecording
```

### waitForAnimationToEnd
Waits for in-progress UI animations to finish before the next command runs.
Use when an element is technically visible but still moving (e.g. a sliding
menu), which can cause a tap to land in the wrong place.

Parameters: `timeout` (ms, optional).

```yaml
- waitForAnimationToEnd:
    timeout: 2000
```

### extendedWaitUntil
Waits for an element to become visible or stop being visible, with a **custom
timeout longer than the default 7-second auto-retry** used by `assertVisible`. Use
for genuinely slow operations (payment processing, large report generation) — don't
use it as a blanket replacement for normal assertions.

```yaml
- extendedWaitUntil:
    visible: "Payment confirmed"
    timeout: 15000
- extendedWaitUntil:
    notVisible: "Loading..."
    timeout: 10000
```

### evalScript / runScript
`evalScript` runs an inline JavaScript expression within the flow (e.g. to set or
increment a variable). `runScript` runs an external `.js` file and can capture its
output. Use only for logic the declarative commands can't express — most test
cases won't need these.

```yaml
- evalScript: ${output.attempt = 0}
- runScript: "./scripts/generate_test_data.js"
```