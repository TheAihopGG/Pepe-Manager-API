# Contributing

## Code style

- Use black formatter
- Follow PEP 8 for Python style guidelines.
- Max line length: 88 characters (Black’s default).
- Use snake_case for variables/functions and PascalCase for classes.

## Documentation

- Add a docstring at the top of every module (*.py file):
```python
__doc__ = """
    Brief description of the module.
    Longer explanation (if needed) covering purpose, key functions, and usage examples.
"""
```
- Use Google-style or NumPy-style for function/method docstrings:
```python
def sum(a: int, b: int) -> int:
    """Adds two integers and returns the result.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        Sum of a and b.
    """
    return a + b
```

## Testing

- Use `unittest` to test your modules
- Create tests in tests dir: `./backend/tests`

## Static Type Checking

- Use mypy for type checking
- Use type hints for all functions/methods/classes

## Commits

- Example:
Feature:
```bash
git commit -m "feat: something"
```

Correction:
```bash
git commit -m "fix: something"
```
