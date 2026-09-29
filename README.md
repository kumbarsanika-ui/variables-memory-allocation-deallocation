# Variables and Memory in Node.js and Python

## What are variables used for?

A variable is a name a program uses to refer to a value. Variables let a program remember information, use it later, perform calculations, make decisions, and pass data between functions. For example, a program might store a user's name, a product's price, a shopping cart, or the result of a calculation.

## A real-life example

Imagine a warehouse with labeled boxes:

- A label such as `shoppingCart` is like a variable name.
- The contents of a box are like a value or object in memory.
- Two labels can point to the same box.
- When no label or other reference can find a box, the runtime can eventually reclaim the space.

This is an analogy, not a literal description of how every variable is stored. A variable's **scope** determines where its name can be used. Whether an object remains in memory depends on whether the program can still reach it.

## Variables in Node.js

Node.js runs JavaScript, usually using the V8 engine.

```js
const productPrice = 10;
const order = { item: "tea", quantity: 2 };

const sameOrder = order;
sameOrder.quantity = 3;
console.log(order.quantity); // 3: both names refer to the same object

// order = {}; // Error: a const binding cannot be reassigned
```

`productPrice` refers to a number, and `order` refers to an object. `const` prevents reassigning the name `order`; it does not make the object immutable. `let` and `const` are block-scoped. `var` is function-scoped (or script-scoped when declared outside a function).

JavaScript engines manage memory automatically. Values and objects that can still be reached by the program remain available. Objects that are no longer reachable can be reclaimed by garbage collection. Setting a variable to `null` removes that variable's reference, but does not directly delete the object:

```js
let order = { item: "tea" };
let anotherName = order;

order = null; // The object is still reachable through anotherName
anotherName = null; // Now it can be reclaimed, at a time chosen by the engine
```

### V8 memory management in Node.js

V8, the JavaScript engine commonly used by Node.js, stores managed JavaScript objects in a garbage-collected heap. It uses generational collection: many short-lived objects are collected in a young generation, while objects that survive longer can be moved to an older generation. V8 finds objects reachable from roots such as active execution contexts and global references; unreachable objects become eligible for collection. The exact timing and internal layout are managed by V8.

## Variables in Python

Python names are bound to objects. Assigning a second name does not automatically copy an object:

```python
product_price = 10
order = {"item": "tea", "quantity": 2}

another_name = order
another_name["quantity"] = 3

print(order["quantity"])  # 3: both names refer to the same dictionary
```

### Reference counting in Python

In the commonly used CPython implementation, Python objects are dynamically allocated and tracked using reference counts. Assigning another name to an object adds a reference; rebinding or deleting a name removes that reference. When an object's reference count reaches zero, CPython can usually reclaim it promptly.

Reference counting alone cannot clean up a cycle of objects that refer to each other. For example, a list can contain a reference to itself; even after the program deletes its name for that list, the cycle still exists. CPython's cyclic garbage collector can find and reclaim such unreachable cycles. Other Python implementations may manage memory differently.

`del` removes a name; it does not guarantee that the object is immediately destroyed:

```python
order = {"item": "tea"}
another_name = order

del order  # The dictionary is still reachable through another_name
del another_name  # No names here refer to the dictionary now
```

Python may reuse freed memory instead of immediately returning it to the operating system.

## Stack and heap

The **stack** and **heap** are useful general concepts for discussing memory, but they are not a promise about the exact physical location of every variable:

- The stack is commonly associated with active function calls and their execution state. When a function returns, its call state is no longer active.
- The heap is memory used for dynamically managed objects, such as JavaScript objects and Python lists or dictionaries. An object can outlive the function that created it if the program still has a reference to it.
- A language runtime or compiler can optimize how values are represented. Avoid assuming that every local variable is literally stored on the stack or every value uses a separate heap allocation.

In both languages, the runtime allocates memory as values and objects are needed. It later makes memory from unreachable or unused objects available for reuse. This is automatic in ordinary Node.js and Python code; there is no general-purpose statement that guarantees an object is immediately erased from memory.

## Garbage collection and deallocation

Garbage collection identifies memory that a program no longer needs and makes it available for reuse. Node.js relies on V8's garbage collector. CPython primarily uses reference counting, with a cyclic garbage collector to handle reference cycles. These are different implementation strategies, but neither gives application code a reliable exact expiry time for an object.

Reclaiming an object also does not necessarily mean the process immediately gives the same memory back to the operating system. The runtime or allocator may keep it available for later allocations. When the process exits, the operating system reclaims the process's memory.

## Scope and memory lifetime

- A local variable name is generally usable only within its function or block.
- A value can remain alive after a local name goes out of scope if another part of the program still refers to it. For example, a returned function can retain access to values from the function that created it (a closure).
- When an object is no longer reachable, the runtime can reclaim its memory. Node.js does this through garbage collection; CPython commonly uses reference counting as well as garbage collection. Exact timing is not guaranteed in either language.
- When the process exits, the operating system reclaims the process's memory.

## Python vs. Node.js memory management

| Question | Node.js | Python |
| --- | --- | --- |
| What is a variable? | A name bound to a value; for objects, the name refers to the object. | A name bound to an object. |
| How long can I use the name? | While it is in scope, including any access preserved by a closure. | While it is in scope, including any access preserved by a closure. |
| Main cleanup strategy | V8 traces references from program roots and collects unreachable objects, using generational collection. | CPython usually reclaims objects when their reference count reaches zero and uses a cyclic garbage collector for unreachable cycles. Other Python implementations may differ. |
| When can an object's memory be reclaimed? | When it is no longer reachable; V8 decides when to collect it. | In CPython, often when its reference count reaches zero; unreachable cycles are collected separately. |
| Can I force an object to be deleted now? | No. Assigning `null` removes a reference, but collection is automatic. | No. `del` removes a name; it does not guarantee immediate object destruction or memory return to the OS. |

**In short:** variables help programs keep and work with data. Scope controls where a name can be used; references determine whether an object is still needed. Neither language gives a general fixed expiry time for a variable's memory, so programs should not depend on an exact deletion time.