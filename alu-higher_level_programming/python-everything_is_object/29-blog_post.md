# Python3: Mutable, Immutable... Everything Is an Object!

![Add a picture here: for example a diagram of two variables pointing to the same box in memory](add-your-picture-url-here)

## Introduction

In Python, everything is an object: integers, strings, lists, functions, even classes. A variable is not a box that contains a value; it is a name that points to an object living somewhere in memory. Understanding this one idea explains a lot of behavior that looks surprising at first, such as why changing a list inside a function changes it for the caller, while incrementing an integer inside a function does not. This post walks through `id` and `type`, mutable and immutable objects, and how Python passes arguments to functions.

## id and type

Every object has an identity and a type. `id()` returns the identity (in CPython, the memory address of the object) and `type()` returns the class of the object:

```python
>>> a = 89
>>> type(a)
<class 'int'>
>>> id(a)        # the number will differ on your machine
139926795932424
>>> b = a
>>> b is a       # same object: same identity
True
>>> id(a) == id(b)
True
```

The `is` operator compares identities, while `==` compares values. Two objects can be equal without being the same object:

```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> l1 == l2
True
>>> l1 is l2
False
>>> l3 = l1
>>> l3 is l1
True
```

## Mutable objects

A mutable object can be changed in place after it is created, and its identity stays the same. Lists, dictionaries and sets are mutable:

```python
>>> l = [1, 2, 3]
>>> id(l)
140213400543048
>>> l.append(4)
>>> l
[1, 2, 3, 4]
>>> id(l)        # same object, new content
140213400543048
```

Because `l2 = l1` only copies the reference, both names see the change:

```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1.append(4)
>>> print(l2)
[1, 2, 3, 4]
```

## Immutable objects

An immutable object cannot be changed after creation. Integers, floats, strings, tuples, booleans and frozensets are immutable. Operations that look like modifications create a new object instead:

```python
>>> a = 1
>>> id(a)
9788992
>>> a += 1       # builds a new int object and rebinds the name a
>>> id(a)
9789024
```

Python also reuses some immutable objects to save memory. CPython keeps one object for each small integer (from -5 to 256), and the empty tuple is a single shared object:

```python
>>> a = 89
>>> b = 89
>>> a is b
True
>>> () is ()
True
```

The result of `is` on equal immutable values depends on how the code is compiled. In a script, identical constants in the same piece of code are merged, so `a = (1, 2)` and `b = (1, 2)` (or two identical string literals) end up pointing to the same object and `a is b` is `True`. In the interactive shell each line is compiled separately, so the same code can give `False`. This is an optimization, not a guarantee, so use `==` to compare values and `is` only for identity (for example `x is None`).

Note that `(1)` is not a tuple, it is just the integer 1 in parentheses. A one-element tuple needs a trailing comma: `(1,)`. A tuple is immutable, but if it holds a mutable object, that inner object can still change.

## Why does it matter, and how differently does Python treat them?

Mutable and immutable objects behave differently when you "change" them. With a mutable object, a method like `append` modifies the object itself, so every name pointing to it sees the change. With an immutable object, there is no in-place change; Python creates a new object and rebinds the name, leaving other names untouched.

The `+` and `+=` operators on lists show the difference clearly:

```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1 = l1 + [4]     # creates a NEW list and rebinds l1
>>> print(l2)
[1, 2, 3]

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1 += [4]         # extends the SAME list in place
>>> print(l2)
[1, 2, 3, 4]
```

It matters for correctness (accidentally sharing a list between two parts of a program), for performance (building a long string with `+=` in a loop creates many temporary objects), and for design (only immutable objects can be dictionary keys, because their hash must never change). To get an independent copy of a list, copy it explicitly:

```python
def copy_list(my_list):
    return my_list[:]
```

Note that this is a shallow copy: the new list holds references to the same inner objects.

## How arguments are passed to functions

Python passes arguments by assignment (sometimes called "pass by object reference"). The parameter is a new local name bound to the same object the caller passed in. What happens next depends on what the function does with it.

If the function mutates a mutable object, the caller sees the change:

```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)    # [1, 2, 3, 4]
```

If the function rebinds the parameter name, only the local name changes, whether the object is mutable or not:

```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)   # [1, 2, 3]
```

With an immutable object such as an integer, `n += 1` cannot modify the original, so it builds a new integer and rebinds the local name `n`:

```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)    # 1
```

The rule of thumb: a function can change the caller's object only if the object is mutable and the function mutates it in place instead of rebinding the name.

## Conclusion

Names point to objects; `id` tells you which object, `type` tells you what kind. Mutable objects change in place and are shared through every name that references them, while immutable objects are replaced by new ones. Function arguments follow the same rules as plain assignment. Once you think in terms of names and objects, behaviors like list aliasing, `+` vs `+=`, and integer caching stop being surprises and become predictable.
