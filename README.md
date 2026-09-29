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