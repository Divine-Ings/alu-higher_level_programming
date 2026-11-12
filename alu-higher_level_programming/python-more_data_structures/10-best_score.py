#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    best_value = None
    for k, v in a_dictionary.items():
        if best_value is None or v > best_value:
            best_key, best_value = k, v
    return best_key
