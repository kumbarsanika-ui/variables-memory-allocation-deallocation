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

```python
x = 10
```

Conceptually, `x` refers to the integer object `10`. Assignment binds the name `x` to that object.

### 2. Are values in Python objects?

Python's data model represents values as objects. Objects have an identity, a type, and a value.

```python
x = 10
name = "Aishu"
marks = 85.5
numbers = [10, 20, 30]

print(id(x))    # Identity for this object's lifetime
print(type(x))  # <class 'int'>
print(x)        # The value: 10
```

`id()` returns an object's identity. In CPython it is commonly related to the object's memory address, but Python does not promise that interpretation. `type()` reports the object's type, and evaluating the name shows its value.

### 3. Built-in data type categories

- Numeric: `int`, `float`, `complex`
- Boolean: `bool`
- Text: `str`
- Sequences: `list`, `tuple`, `range`
- Sets: `set`, `frozenset`
- Mapping: `dict`
- Binary: `bytes`, `bytearray`, `memoryview`
- Special value: `None` (whose type is `NoneType`)

### 4. Numeric types

```python
age = 25             # int
count = -10          # int
price = 99.0         # float
percentage = 88.75   # float
z = 3 + 4j           # complex
```

### 5. Boolean type

Boolean values are spelled `True` and `False` with initial capitals.

```python
is_active = True
is_logged_in = False

print(bool(0))       # False
print(bool(""))      # False
print(bool("hello"))  # True
```

### 6. Strings

A string is an immutable sequence of characters. Indexing starts at zero.

```python
name = "Aishu"
print(name[0])  # A
print(name[1])  # i
```

### 7. Lists

Lists are ordered and mutable, allow duplicates, and can contain values of different types.

```python
numbers = [10, 20, 30]
data = [10, "python", 25.5, True]
```

### 8. Tuples

Tuples are ordered and immutable, and they allow duplicates.

```python
point = (10, 20)
```

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

```python
result = None
```

### 12. Mutable and immutable objects

An immutable object cannot be changed after it is created. Common immutable types include `int`, `float`, `bool`, `str`, `tuple`, and `frozenset`.

Mutable objects can be changed in place. Common mutable types include `list`, `set`, `dict`, and `bytearray`.

### 13. Rebinding a name

When an immutable value appears to change, the name is usually being bound to a different object; the original object was not modified.

```python
x = 10
x = 20
```

After the first assignment, `x` refers to `10`; after the second, it refers to `20`. The integer `10` was not changed.

### 14. Two names bound to one immutable object

```python
a = 10
b = a
a = 20

print(a)  # 20
print(b)  # 10
```

Initially, both names refer to the integer object `10`. Rebinding `a` does not rebind `b`.

### 15. Two names referring to one mutable object

```python
a = [10, 20]
b = a
b.append(30)
print(a)  # [10, 20, 30]
```

Both names refer to the same list. `append()` mutates that list, so the change is visible through either name.

### 16. `==` versus `is`

`==` compares values for equality. `is` checks whether two names refer to the very same object.

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True: equal contents
print(a is b)  # False: distinct list objects
```

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

```python
numbers = [1, 2, 3]
b = numbers
del numbers
print(b)  # [1, 2, 3]
```

The list remains reachable through `b`.

### 22. When can an object be reclaimed?

An object becomes eligible for reclamation when it is no longer reachable. In CPython, an object with no remaining references is often reclaimed promptly, but cycles and implementation details can affect when that happens. The exact timing is not a general Python guarantee, and reclaimed memory is not necessarily returned to the operating system immediately.

```python
numbers = [1, 2, 3]
b = numbers
del numbers
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