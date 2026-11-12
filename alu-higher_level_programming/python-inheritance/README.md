# python-inheritance

Python project on inheritance: `dir()`, `isinstance()`, `issubclass()`,
subclassing built-in types, base classes, `super()`, and doctests.

## Requirements
- Ubuntu 20.04 LTS, python3 (3.8.5)
- pycodestyle 2.7.*
- First line of every Python file: `#!/usr/bin/python3`
- All files end with a new line and all Python files are executable
- All modules, classes and functions are documented
- Doctests: `python3 -m doctest -v ./tests/1-my_list.txt`

## Files
| File | Description |
|------|-------------|
| 0-lookup.py | Returns the attributes and methods of an object |
| 1-my_list.py | `MyList` (inherits from `list`) with `print_sorted()` |
| 2-is_same_class.py | True if the object is exactly an instance of the class |
| 3-is_kind_of_class.py | True if the object is an instance of the class or a subclass |
| 4-inherits_from.py | True if the object is an instance of a subclass only |
| 5-base_geometry.py | Empty class `BaseGeometry` |
| 6-base_geometry.py | `BaseGeometry` with unimplemented `area()` |
| 7-base_geometry.py | Adds `integer_validator()` |
| 8-rectangle.py | `Rectangle` inheriting from `BaseGeometry` |
| 9-rectangle.py | `Rectangle` with `area()` and `__str__` |
| 10-square.py | `Square` inheriting from `Rectangle` |
| 11-square.py | `Square` with its own `__str__` |
| tests/1-my_list.txt | Doctests for `1-my_list.py` |
| tests/7-base_geometry.txt | Doctests for `7-base_geometry.py` |
