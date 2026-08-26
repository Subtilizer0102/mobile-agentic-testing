**Test case:** "Log into the app with a valid username and password, allow the
notification permission if it's requested, and confirm the home screen loads with
the welcome message visible."

**Output:**
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
- tapOn: "Log In"
- runFlow:
    when:
      visible: "Allow Notifications"
    commands:
      - tapOn: "Allow"
- assertVisible: "Welcome back"
```

**Test case:** "Search for 'wireless headphones' in the shopping app, scroll down
until the third result is visible, and add it to the cart. Confirm the cart badge
shows 1 item."

**Output:**
```yaml
appId: com.example.shopping
---
- launchApp
- tapOn: "Search"
- inputText: "wireless headphones"
- pressKey: enter
- scrollUntilVisible:
    element:
      id: "search_result_item"
      index: 2
    direction: DOWN
- tapOn:
    id: "search_result_item"
    index: 2
- tapOn: "Add to Cart"
- assertVisible:
    id: "cart_badge"
    text: "1"
```