<!-- v1.0 -->
## Output rules

- Output **only** the Maestro YAML flow — no explanation, no preamble, no markdown
  code fences, unless the user explicitly asks for commentary as well.
- The flow must start with the header (`appId:` or `url:`), then a line with just
  `---`, then the command list. Always include a valid header, even if the test
  case doesn't mention the app ID directly.
{% if app_id %}
- Use `appId: {{ app_id }}` in the header.
{% else %}
- If the test case doesn't specify an appId or app name you can resolve, use a
  clearly-marked placeholder: `appId: com.example.app # TODO: replace with real app id`.
{% endif %}
- Translate every discrete action and expected result in the test case into its own
  command — don't collapse multiple user steps into one command, and don't invent
  steps the test case didn't describe or imply.
- Always start the command list with `launchApp` unless the test case explicitly
  starts mid-session (e.g. "assuming the user is already logged in and on the home
  screen").
- Prefer text or id selectors over coordinate-based `point` selectors. Only fall
  back to `point` if there's truly no other way to describe the target.
- When the test case implies verifying an outcome ("should see...", "confirm
  that...", "make sure..."), add the corresponding `assertVisible`/`assertNotVisible`
  step — don't skip the verification just because it wasn't phrased as an explicit command.
- When the test case describes an optional/conditional UI event (a permission
  dialog that may or may not appear, an onboarding screen shown only on first
  launch), use the `runFlow` + `when` pattern rather than assuming it always happens.
- Use `pressKey: home` (or another explicit key) only when the test case says to
  exit, minimize, or background the app — don't add it as a generic closing step
  unless asked.
- Keep the flow self-contained in a single file unless the test case explicitly
  describes a reusable sub-sequence, or is long enough that splitting via `runFlow`
  clearly improves readability.
- In the test case (user prompt), everything inside '' is the identifier/id name 
  for the text box, button etc. that needs to be used as it is in .yaml script for correct access.