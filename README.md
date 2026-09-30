<<<<<<< HEAD
# Python Variables, Objects, and Memory Management

This guide explains how Python names refer to objects, how built-in types behave, and how Python manages memory. The examples use standard Python syntax and focus on concepts that are useful for beginners and interviews.

## 1. What is a variable in Python?

A Python variable is a **name bound to an object**. It is useful to think of a name as a label referring to an object, rather than a box that contains a value.
=======
# Variables, Memory Allocation, and Deallocation

Variables let a program give names to values so it can store state, calculate results, and pass data between functions. In both Node.js and Python, a variable is best understood as a **name bound to a value**. It is not necessarily a box that contains the value itself.

```js
let first = { score: 10 };
let second = first;
second.score = 20;
console.log(first.score); // 20: both names refer to the same object
```

```python
first = {"score": 10}
second = first
second["score"] = 20
print(first["score"])  # 20: both names refer to the same object
```

## Scope and lifetime

Two different lifetimes are useful to distinguish:

- **Name lifetime:** how long a name can be accessed in its scope. A local name usually cannot be used after its function returns.
- **Object lifetime:** how long the value remains in memory. An object may outlive the function that created it if another reference still points to it, such as a global variable or a closure.

There is no general expiry timer for variables. When an object is no longer reachable by the program, it becomes eligible for memory reclamation. The runtime controls when reclamation occurs, so becoming unreachable does not always mean memory is released at that exact moment.

```python
def make_list():
    values = [1, 2, 3]
    return values

items = make_list()  # The list stays alive because `items` refers to it.
```

## Memory allocation in Node.js

Node.js runs JavaScript using the V8 engine.

- Function calls create execution contexts. The engine manages local bindings and may use stack-like storage, registers, or optimized representations. The language does not guarantee that every local variable occupies a literal stack slot.
- Objects, arrays, and functions are generally allocated in memory managed by V8, commonly described as the heap. Primitive values may use engine-specific representations.
- V8's garbage collector finds objects that are no longer reachable from program roots, such as active execution contexts, global values, and retained closures. It can reclaim those objects.
- V8 uses a generational garbage collector. Many short-lived objects are collected in a young generation; objects that survive may be moved to an older generation and collected differently.
- JavaScript code does not control the exact time garbage collection runs.

A closure can keep a function's local state alive after the function returns:

```js
function makeCounter() {
	let count = 0;
	return () => ++count;
}

const next = makeCounter(); // `count` remains reachable through `next`.
console.log(next()); // 1
```

## Python variables, objects, and built-in types

### 1. What is a variable in Python?

A variable is a **name bound to an object**. It is not a box that contains the object itself.
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080

```python
x = 10
```

<<<<<<< HEAD
Here, `x` refers to the integer object `10`.

## 2. Is everything in Python an object?

In Python, values such as integers, strings, floats, lists, and functions are objects. An object has an identity, a type, and a value.
=======
Conceptually, `x` refers to the integer object `10`. Assignment binds the name `x` to that object.

### 2. Are values in Python objects?

Python's data model represents values as objects. Objects have an identity, a type, and a value.
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080

```python
x = 10
name = "Aishu"
marks = 85.5
numbers = [10, 20, 30]

<<<<<<< HEAD
print(id(x))      # identity for this object's lifetime
print(type(x))    # <class 'int'>
print(x)          # value: 10
```

`id()` returns an identity for an object. In CPython, this is commonly its memory address, but Python code should not depend on that implementation detail. `type()` reports its type, and printing the object displays its value.

## 3. What are Python's built-in data types?

Common built-in types can be grouped like this:
=======
print(id(x))    # Identity for this object's lifetime
print(type(x))  # <class 'int'>
print(x)        # The value: 10
```

`id()` returns an object's identity. In CPython it is commonly related to the object's memory address, but Python does not promise that interpretation. `type()` reports the object's type, and evaluating the name shows its value.

### 3. Built-in data type categories
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080

- Numeric: `int`, `float`, `complex`
- Boolean: `bool`
- Text: `str`
- Sequences: `list`, `tuple`, `range`
- Sets: `set`, `frozenset`
- Mapping: `dict`
- Binary: `bytes`, `bytearray`, `memoryview`
<<<<<<< HEAD
- Null value: `NoneType` (the type of `None`)

## 4. Numeric types
=======
- Special value: `None` (whose type is `NoneType`)

### 4. Numeric types
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080

```python
age = 25             # int
count = -10          # int
price = 99.0         # float
percentage = 88.75   # float
z = 3 + 4j           # complex
```

<<<<<<< HEAD
## 5. Boolean values

Python's Boolean values are `True` and `False` (capitalized).
=======
### 5. Boolean type

Boolean values are spelled `True` and `False` with initial capitals.
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080

```python
is_active = True
is_logged_in = False

print(bool(0))       # False
print(bool(""))      # False
<<<<<<< HEAD
print(bool("hello")) # True
```

Many values have a truth value. For example, zero and empty containers are falsey; most other values are truthy.

## 6. Strings

A string is an immutable sequence of characters. Use square brackets to access characters by index:
=======
print(bool("hello"))  # True
```

### 6. Strings

A string is an immutable sequence of characters. Indexing starts at zero.
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080

```python
name = "Aishu"
print(name[0])  # A
print(name[1])  # i
```

<<<<<<< HEAD
An attempt to assign to `name[0]` raises a `TypeError`; create a new string instead.

## 7. Lists

Lists are ordered and mutable, allow duplicate values, and can contain values of different types.
=======
### 7. Lists

Lists are ordered and mutable, allow duplicates, and can contain values of different types.
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080

```python
numbers = [10, 20, 30]
data = [10, "python", 25.5, True]
```

<<<<<<< HEAD
## 8. Tuples

Tuples are ordered and immutable, and they allow duplicate values.
=======
### 8. Tuples

Tuples are ordered and immutable, and they allow duplicates.
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080

```python
point = (10, 20)
```

<<<<<<< HEAD
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
=======
### 9. Sets

Sets are mutable collections of unique elements. They are not indexed by position.

```python
numbers = {10, 10, 20, 30}
print(numbers)  # Contains 10, 20, and 30; order is not a positional guarantee
```

Use `frozenset` for an immutable set.

### 10. Dictionaries

Dictionaries store key-value pairs.

```python
student = {
	"id": 101,
	"name": "Aishu",
	"marks": 85.5,
}
```

### 11. `None`

`None` represents the absence of a value. It is different from `0`, `False`, an empty string (`""`), and an empty list (`[]`); each has a different meaning and type.
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080

```python
result = None
```

<<<<<<< HEAD
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
=======
### 12. Mutable and immutable objects

An immutable object cannot be changed after it is created. Common immutable types include `int`, `float`, `bool`, `str`, `tuple`, and `frozenset`.

Mutable objects can be changed in place. Common mutable types include `list`, `set`, `dict`, and `bytearray`.

### 13. Rebinding a name

When an immutable value appears to change, the name is usually being bound to a different object; the original object was not modified.
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080

```python
x = 10
x = 20
```

After the first assignment, `x` refers to `10`; after the second, it refers to `20`. The integer `10` was not changed.

<<<<<<< HEAD
## 14. Two names referring to one object
=======
### 14. Two names bound to one immutable object
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080

```python
a = 10
b = a
<<<<<<< HEAD
```

Both names refer to the integer object representing `10`. If `a` is later rebound to `20`, `b` still refers to `10`.

```python
a = 20
print(b)  # 10
```

## 15. Aliasing a mutable object

Assigning a list to another name does not make a copy. Both names refer to the same list:
=======
a = 20

print(a)  # 20
print(b)  # 10
```

Initially, both names refer to the integer object `10`. Rebinding `a` does not rebind `b`.

### 15. Two names referring to one mutable object
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080

```python
a = [10, 20]
b = a
b.append(30)
<<<<<<< HEAD

print(a)  # [10, 20, 30]
```

`append()` changes that list in place, so the change is visible through either name.

## 16. `==` versus `is`

- `==` checks whether two objects have equal values.
- `is` checks whether two names refer to the very same object.
=======
print(a)  # [10, 20, 30]
```

Both names refer to the same list. `append()` mutates that list, so the change is visible through either name.

### 16. `==` versus `is`

`==` compares values for equality. `is` checks whether two names refer to the very same object.
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True: equal contents
print(a is b)  # False: distinct list objects
```

<<<<<<< HEAD
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
=======
Use `is None` when checking for `None`. Do not use `is` as a substitute for value equality.

### 17. Where does Python use memory?

A Python program uses memory for objects such as integers, strings, dictionaries, lists, and functions, as well as for its runtime and execution state. Python manages object memory dynamically. In CPython, objects are managed by Python's memory allocator, which obtains memory from the process and ultimately the operating system. Exact implementation details vary across Python implementations.

### 18. Reference counting in CPython

CPython primarily uses reference counting. Conceptually, when another name refers to an object, that is another reference; removing a reference can decrease the count.

```python
a = [1, 2, 3]
b = a  # Both names refer to the same list.
del b  # Removes the name b; a still refers to the list.
```

This is a conceptual explanation, not a reliable way to inspect an exact count: temporary references and implementation details affect observed counts.

### 19. Garbage collection

Garbage collection is automatic memory management that reclaims objects the program can no longer reach. Python programmers normally do not manually free object memory.

### 20. Reference counting and cyclic garbage collection

Reference counting can reclaim many objects when their reference count reaches zero. It cannot, by itself, reclaim objects that only refer to each other in a cycle. CPython's cyclic garbage collector can detect and collect many unreachable cycles.

```python
a = []
a.append(a)  # The list refers to itself, creating a cycle.
```

### 21. What does `del` do?

`del` removes a name or reference; it does not guarantee that the object is immediately destroyed.
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080

```python
numbers = [1, 2, 3]
b = numbers
del numbers
<<<<<<< HEAD

print(b)  # [1, 2, 3]
```

## 22. When can an object be reclaimed?

When no references to an object remain, it is no longer reachable through those references and its memory can be reclaimed. In CPython, an object with no references is often reclaimed promptly, except for cases such as reference cycles. Other Python implementations may behave differently, so do not rely on exact timing.
=======
print(b)  # [1, 2, 3]
```

The list remains reachable through `b`.

### 22. When can an object be reclaimed?

An object becomes eligible for reclamation when it is no longer reachable. In CPython, an object with no remaining references is often reclaimed promptly, but cycles and implementation details can affect when that happens. The exact timing is not a general Python guarantee, and reclaimed memory is not necessarily returned to the operating system immediately.
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080

```python
numbers = [1, 2, 3]
b = numbers
del numbers
<<<<<<< HEAD
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
=======
del b  # No longer reachable through these two names.
```

### 23. A conceptual model

**Name -> object (identity, type, value) -> managed memory -> unreachable object may be reclaimed.**

This is a mental model, not a promise about the exact internal storage or reclamation timing.

### 24. Why doesn't `del numbers` necessarily destroy an object immediately?

Because `del numbers` removes the name `numbers`; other names, containers, or parts of the program may still refer to the object. If it becomes unreachable, the runtime can reclaim it. CPython often reclaims non-cyclic objects promptly through reference counting, while cyclic garbage may be collected later. Python also does not guarantee that reclaimed memory is immediately returned to the operating system.

## Memory allocation in Python

Python's language specification does not require one particular memory-management implementation. The following describes **CPython**, the most commonly used implementation.

- Names are bindings in a scope, such as a function's local scope or a module's global scope.
- Objects are managed by Python and are typically allocated on the heap. As in JavaScript, the simple rule "variables are on the stack and objects are on the heap" is not guaranteed by the language.
- CPython primarily uses **reference counting**. References to an object are tracked; when the count reaches zero, CPython can usually reclaim the object promptly.
- Reference counting alone cannot reclaim unreachable reference cycles. CPython also has a cyclic garbage collector to detect and collect many such cycles.
- Other Python implementations can use different memory-management strategies. Code should not rely on immediate cleanup as a universal Python guarantee.

## Real-life example: an online shopping cart

Imagine a shopping cart as a basket of items. A variable is like a label pointing to that basket. Two labels can point to the same basket; removing one label does not remove the basket if another label still points to it.

### Node.js

```js
function createCart() {
	const cart = { items: ["book"] }; // Allocate a cart object.
	const checkoutCart = cart; // Both names refer to the same object.
	return checkoutCart;
}

let activeCart = createCart(); // The object outlives createCart().
const orderHistory = [activeCart]; // History keeps the object reachable.
activeCart = null; // Removes this reference, but history still holds it.
orderHistory.length = 0; // No longer retained here; V8 may collect it later.
```

The function's local names stop being available when `createCart` returns, but the returned cart remains alive through `activeCart`. Later, `orderHistory` keeps it alive even after `activeCart` is set to `null`. Once no reachable part of the program refers to the cart, V8 can reclaim it during a future garbage-collection cycle.

### Python

```python
def create_cart():
		cart = {"items": ["book"]}  # Allocate a cart object.
		checkout_cart = cart  # Both names refer to the same object.
		return checkout_cart

active_cart = create_cart()  # The object outlives create_cart().
order_history = [active_cart]  # History keeps the object referenced.
del active_cart  # Removes this name; order_history still refers to the object.
order_history.clear()  # Removes the remaining application reference.
```

In CPython, when the last reference to an object is removed, reference counting can usually reclaim it promptly. `del active_cart` only removes the name `active_cart`; it does not force the object to be destroyed if `order_history` or another name still refers to it. Reclaiming the object's memory also does not guarantee that Python immediately returns that memory to the operating system.

### Stack and heap analogy

Think of a function call as a worker's temporary clipboard and the cart object as a basket stored in a shared stockroom. The clipboard holds temporary task details while the worker is handling a request. The basket can remain after that task ends if another worker or the order-history system still has its location. This is only an analogy: language runtimes optimize storage, so it is not a literal rule that every variable lives on a stack and every object lives on a heap.

## Comparison

| Topic | Node.js | Python (CPython) |
| --- | --- | --- |
| Variable | A name bound to a value | A name bound to an object/value |
| When scope ends | The name may stop being accessible | The name may stop being accessible |
| How unused objects are reclaimed | V8 garbage-collects unreachable objects | Reference counting often reclaims objects promptly; cyclic GC handles many cycles |
| Exact cleanup time | Not guaranteed | Often prompt in CPython, but not guaranteed across Python implementations |
| Common way to retain unwanted memory | Keeping objects reachable unintentionally | Keeping references, or retaining objects that participate in cycles |

## Memory leaks

In garbage-collected languages, a memory leak often means that the program unintentionally keeps references to data it no longer needs. A growing cache, an event-listener collection that is never cleared, or a closure retaining a large object can all keep memory reachable and prevent reclamation.

Garbage collection reclaims memory for objects the runtime considers unreachable. It does not guarantee that the process immediately returns that memory to the operating system; a runtime may keep reclaimed space available for future allocations.
>>>>>>> c0fb686431bcb9b640cf41b3a530d4031041d080
