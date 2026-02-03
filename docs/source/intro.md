# Furo Theme Showcase

This page demonstrates how your custom styles, fonts, and colors look in action. We are currently using **Inter** for body text and **JetBrains Mono** for code.

---

## 1. Admonitions (Custom Rounded Corners)

These boxes use the `8px` border-radius and the thicker left accent line we defined in the CSS.

```{note}
This is a standard note using backticks.
```

```{warning}
This is a warning note using backticks.
```

```{danger}
This is a danger note using backticks.
```

---

## 2. Code Blocks (JetBrains Mono)

Check out the syntax highlighting and the rounded corners on the code container.

```python
def hello_furo(name: str) -> None:
    """
    A simple function to demonstrate JetBrains Mono
    and contextual ligatures.
    """
    greeting = f"Hello, {name}!"
    print(greeting)

# Call the function
hello_furo("Documentation")
```