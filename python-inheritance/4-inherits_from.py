#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Check if object belongs to a subclass."""
    return isinstance(obj, a_class) and type(obj) is not a_class
