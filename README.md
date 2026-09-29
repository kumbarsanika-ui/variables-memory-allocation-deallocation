# Python Variables, Objects, and Memory Management

This guide explains how Python names refer to objects, how built-in types behave, and how Python manages memory. The examples use standard Python syntax and focus on concepts that are useful for beginners and interviews.

## 1. What is a variable in Python?

A Python variable is a **name bound to an object**. It is useful to think of a name as a label referring to an object, rather than a box that contains a value.

```python
x = 10
```

Here, `x` refers to the integer object `10`.

## 2. Is everything in Python an object?

In Python, values such as integers, strings, floats, lists, and functions are objects. An object has an identity, a type, and a value.

```python
x = 10
name = "Aishu"
marks = 85.5
numbers = [10, 20, 30]

print(id(x))      # identity for this object's lifetime
print(type(x))    # <class 'int'>
print(x)          # value: 10
```

`id()` returns an identity for an object. In CPython, this is commonly its memory address, but Python code should not depend on that implementation detail. `type()` reports its type, and printing the object displays its value.

## 3. What are Python's built-in data types?

Common built-in types can be grouped like this:

- Numeric: `int`, `float`, `complex`
- Boolean: `bool`
- Text: `str`
- Sequences: `list`, `tuple`, `range`
- Sets: `set`, `frozenset`
- Mapping: `dict`
- Binary: `bytes`, `bytearray`, `memoryview`
- Null value: `NoneType` (the type of `None`)

## 4. Numeric types

```python
age = 25             # int
count = -10          # int
price = 99.0         # float
percentage = 88.75   # float
z = 3 + 4j           # complex
```

## 5. Boolean values

Python's Boolean values are `True` and `False` (capitalized).

```python
is_active = True
is_logged_in = False

print(bool(0))       # False
print(bool(""))      # False
print(bool("hello")) # True
```

Many values have a truth value. For example, zero and empty containers are falsey; most other values are truthy.

## 6. Strings

A string is an immutable sequence of characters. Use square brackets to access characters by index:

```python
name = "Aishu"
print(name[0])  # A
print(name[1])  # i
```

An attempt to assign to `name[0]` raises a `TypeError`; create a new string instead.

## 7. Lists

Lists are ordered and mutable, allow duplicate values, and can contain values of different types.

```python
numbers = [10, 20, 30]
data = [10, "python", 25.5, True]
```

## 8. Tuples

Tuples are ordered and immutable, and they allow duplicate values.

```python
point = (10, 20)
```

## 9. Sets

Sets are mutable collections of unique elements. They do not support positional indexing. An empty set is written as `set()` because `{}` creates an empty dictionary.

```python
numbers = {10, 10, 20, 30}
print(numbers)  # contains 10, 20, and 30; display order is not guaranteed
```

## 10. Dictionaries

Dictionaries store key-value pairs. Keys must be hashable; values can be of any type.

```python
student = {
    "id": 101,
    "name": "Aishu",
    "marks": 85.5,
}
```

## 11. `None`

`None` represents the absence of a value. It is a distinct object, not the same as `0`, `False`, an empty string, or an empty list.

```python
result = None
```

Use `is None` when checking for it:

```python
if result is None:
    print("No result yet")
```

## 12. Mutable and immutable objects

An immutable object's value cannot be changed after it is created. Common immutable types include `int`, `float`, `bool`, `str`, `tuple`, and `frozenset`.

Mutable objects can be changed in place. Common mutable types include `list`, `dict`, `set`, and `bytearray`.

## 13. Rebinding a name

When you assign a new value to a name, Python binds the name to another object. It does not modify the original integer:

```python
x = 10
x = 20
```

After the first assignment, `x` refers to `10`; after the second, it refers to `20`. The integer `10` was not changed.

## 14. Two names referring to one object

```python
a = 10
b = a
```

Both names refer to the integer object representing `10`. If `a` is later rebound to `20`, `b` still refers to `10`.

```python
a = 20
print(b)  # 10
```

## 15. Aliasing a mutable object

Assigning a list to another name does not make a copy. Both names refer to the same list:

```python
a = [10, 20]
b = a
b.append(30)

print(a)  # [10, 20, 30]
```

`append()` changes that list in place, so the change is visible through either name.

## 16. `==` versus `is`

- `==` checks whether two objects have equal values.
- `is` checks whether two names refer to the very same object.

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True: equal contents
print(a is b)  # False: distinct list objects
```

Use `is` for identity checks such as `value is None`, not as a general replacement for `==`.

## 17. Where does Python use memory?

While a Python program runs, memory is used for objects such as integers, strings, lists, dictionaries, and functions, as well as runtime bookkeeping. In CPython, objects are managed by Python's memory allocator, which obtains memory from the underlying process and operating system. Exact allocation details differ between Python implementations.

## 18. Reference counting in CPython

CPython primarily uses reference counting. Each object tracks references to it. Assigning another name creates another reference; removing a reference decreases the count.

```python
a = [1, 2, 3]
b = a  # a and b refer to the same list
del b  # removes the name b; a still refers to the list
```

This describes CPython's implementation, not a guarantee that every Python implementation uses reference counting in the same way.

## 19. What is garbage collection?

Garbage collection is automatic management that identifies objects that are no longer needed and makes their memory available for reuse. In Python, programmers normally do not manually free object memory.

## 20. Reference counting and cyclic garbage collection

Reference counting can reclaim an object when its reference count reaches zero. But a group of objects can refer to one another and keep their counts above zero even when the group is unreachable from the rest of the program. CPython's cyclic garbage collector can detect and clean up many such cycles.

```python
items = []
items.append(items)  # the list refers to itself
```

The `gc` module provides controls for CPython's cyclic garbage collector, but most programs do not need to manage it directly.

## 21. What does `del` do?

`del` removes a name or an item; it does not directly command Python to destroy an object. If another reference exists, the object remains accessible:

```python
numbers = [1, 2, 3]
b = numbers
del numbers

print(b)  # [1, 2, 3]
```

## 22. When can an object be reclaimed?

When no references to an object remain, it is no longer reachable through those references and its memory can be reclaimed. In CPython, an object with no references is often reclaimed promptly, except for cases such as reference cycles. Other Python implementations may behave differently, so do not rely on exact timing.

```python
numbers = [1, 2, 3]
b = numbers
del numbers
del b
```

After both names are removed, neither name refers to the list. Other references could still exist elsewhere.

## 23. A useful mental model

```text
name -> object (identity, type, value)
                 |
                 v
       memory managed by Python
                 |
        object becomes unreachable
                 |
       memory may be reclaimed/reused
```

Names refer to objects; objects occupy memory; the runtime manages that memory as objects are used and become unreachable.

## 24. If Python has garbage collection, why doesn't `del numbers` always destroy an object immediately?

Because `del numbers` removes the name `numbers`; it does not necessarily remove every reference to the object. Another name, a container, or a function may still refer to it. Cyclic references can also keep objects alive until the cyclic garbage collector handles them.

Even after an object is reclaimed, Python's allocator may keep the freed memory available for reuse instead of returning it immediately to the operating system. Garbage collection is about making unreachable objects' memory reusable; it is not a promise that process memory usage will instantly decrease.

## Key takeaways

- A variable in Python is a name bound to an object.
- Objects have identity, type, and value.
- Assignment can create another reference rather than a copy.
- Mutable objects can change in place; immutable objects cannot.
- `==` compares values, while `is` compares identity.
- `del` removes a reference (such as a name); it does not guarantee immediate destruction or return of memory to the OS.
- CPython uses reference counting and a cyclic garbage collector; implementation details vary across Python implementations.