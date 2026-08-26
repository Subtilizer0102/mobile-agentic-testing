<!-- v1.0 -->
## Maestro selectors

Selectors identify which UI element a command should act on. Maestro reads the
device's accessibility tree, so selectors should target what a real user would see
or what's exposed as an accessibility identifier — never raw pixel layout unless
nothing else is possible.

Any command that takes a target (`tapOn`, `assertVisible`, `swipe` with `from`, etc.)
accepts either:
- a **shorthand string** — treated as a `text` match, e.g. `tapOn: "Login"`
- a **map** with one or more selector properties combined (AND logic by default).

**Prefer shorthand string** notation unless specified or required. So try **NOT** to do:

```yaml
- tapOn: 
    id: 'Login'
```

### Core selectors

| Selector | Matches | Notes |
|---|---|---|
| `text` | Visible text or accessibility label/description | Regex by default (escape special chars like `$`, `[` with `\`). |
| `id` | Accessibility identifier (Android resource ID / iOS `accessibilityIdentifier`) | Best choice for icons, dynamic content, or localized apps — stays stable across languages. Regex by default. |
| `index` | The Nth match (0-based) when multiple elements match the same criteria | e.g. third "Add to Cart" button: `{ text: "Add to Cart", index: 2 }` |
| `point` | A specific screen coordinate | Relative `"50%,50%"` or absolute `"100,200"` px. Last resort — prefer text/id since coordinates break across devices/screen sizes. |
| `css` | Web only — standard CSS selector | Not regex-based. |

### State property selectors

Combine with a core selector to require a specific element state:

| Selector | Meaning |
|---|---|
| `enabled: true / false` | Element is (not) interactable/clickable |
| `checked: true / false` | Checkbox/switch/radio is (not) checked |
| `selected: true / false` | Element is (not) in a selected state |
| `focused: true / false` | Element (does not have) keyboard focus |

```yaml
- assertVisible:
    text: "My Button"
    enabled: true
```

### Relational (position/hierarchy) selectors

Use when an element has no unique, stable text or id — anchor off a nearby stable element instead.

| Selector | Matches |
|---|---|
| `above: <selector>` | A view above the given anchor |
| `below: <selector>` | A view below the given anchor |
| `leftOf: <selector>` | A view to the left of the given anchor |
| `rightOf: <selector>` | A view to the right of the given anchor |
| `containsChild: <selector>` | A view that has a **direct child** matching the given selector |
| `childOf: <selector>` | A view that is a child of the given parent selector |
| `containsDescendants: [<selector>, ...]` | A view that contains all listed descendant views anywhere below it |

```yaml
# Tap the input located below the "Email" label
- tapOn:
    below: "Email"

# Tap the "Add to Basket" button that belongs to the "Awesome Shoes" product card,
# not just any "Add to Basket" button on the screen
- tapOn:
    text: "Add to Basket"
    below: "Awesome Shoes"
```

### Traits (descriptive shape)

```yaml
- tapOn:
    traits: text          # element that contains some text
- tapOn:
    traits: long-text      # element with 200+ characters of text
- tapOn:
    traits: square          # roughly square element (e.g. icon button)
```

### Selector strategy (use in this priority order)

1. **Visible text** — most readable, self-documenting, matches what the test case describes.
2. **`id`** — for icons, images, or when the app is localized into multiple languages.
3. **Relational selectors** — when several elements share the same text/id and you need to disambiguate via a stable anchor (e.g. "the delete icon next to Item 3").
4. **`point` (coordinates)** — only if no accessible selector exists.