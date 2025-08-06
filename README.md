# Scientist Simulation Core (lab_core)

A Python module simulating scientists and their research activity, featuring:

- A `Scientist` class with domain logic
- Custom context manager for logging (`FileLogger`)
- Decorators for logging function calls
- A data generator for bulk scientist creation
- Full `pytest` test suite with fixtures and parameterized cases

---

## Project Structure

```yaml
lab_core/
├── context.py
├── scientist.py
├── generator.py
├── decorators.py
├── exceptions.py
tests/
├── __init__.py
├── task.md
├── test_scientist.py
├── test_decorators.py
├── test_generator.py
├── test_file_logger.py
```

---

## Features

### `Scientist` class

Models a scientist with:

- Field validation
- Impact level management
- Publishing and promotion logic
- Comparison operators (`==`, `<`, `>`)
- String and repr output

---

### Generator

`generate_scientists(number=N)`  
Yields N randomized scientist objects using realistic name and field patterns.

---

### Logging & Decorators

- `@log_calls`: Logs decorated function calls to a file
- `FileLogger`: Custom context manager used by the decorator

Log file format:

```[2025-08-06 13:45:12] Called sample_method(args=[1, 2], kwargs={'x': 3})```

---

## Testing

Uses `pytest` for all tests.

### To run all tests:

Go to the project directory and run `pytest` in the terminal.

### Test coverage includes:

- Valid/invalid object creation 
- Attribute setters/getters
- Logging and decorator behavior
- Generator return type and output
- Context manager functionality

### Example usage

```bash
from lab_core.scientist import Scientist

sc = Scientist("Marie Curie", field="physics", publications=10, experience_years=15)
print(sc)
sc.promote()
sc.publish()
```
or
```bash
from lab_core.generator import generate_scientists

for s in generate_scientists(number=5):
    print(s)
```