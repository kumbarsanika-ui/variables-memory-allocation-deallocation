# Variables, Memory Allocation, and Deallocation

This project explains one of the most important ideas in programming: how variables use memory and how that memory is later released when it is no longer needed.

## Overview

A variable is a name used to store data in a program. That data may be a number, a string, a list, an object, or a reference to another value. At runtime, the language environment decides where that data lives and when it is safe to reclaim the memory.

The main ideas covered here are:

- What a variable is
- How variables are assigned and referenced
- How memory is allocated
- How memory is deallocated or reclaimed
- Why scope and reachability matter
- How different runtimes manage this differently

## Why variables matter

Variables allow programs to:

- Store user input
- Track state
- Perform calculations
- Pass data between functions
- Keep information alive while needed

Without variables, a program could not meaningfully remember or reuse values while it runs.

## Variables and references

A variable is not always the value itself. In many languages, a variable is a name that points to a value or object.

```js
const item = { name: "book", price: 20 };
const sameItem = item;

sameItem.price = 25;
console.log(item.price); // 25
```

Here, `item` and `sameItem` refer to the same object. The object is not copied; both names point to the same underlying data.

```python
book = {"name": "book", "price": 20}
copy_of_book = book

copy_of_book["price"] = 25
print(book["price"])  # 25
```

The same idea appears in Python: both names refer to the same dictionary object.

## Scope vs. lifetime

A variable's scope defines where it can be used. Its lifetime describes how long the value remains valid.

- A variable may be limited to a block, function, or module.
- A value may continue to exist even after a name goes out of scope if another reference still points to it.
- When no references remain, the runtime may reclaim the memory automatically.

```js
function createCounter() {
  let count = 0;

  return function () {
    count += 1;
    return count;
  };
}

const counter = createCounter();
console.log(counter());
```

In this example, the inner function keeps access to `count` even after `createCounter` returns.

## Memory allocation

Memory allocation means reserving storage for data while a program runs.

Common allocation patterns include:

- Primitive values such as numbers and strings are often stored as part of a variable's local state.
- Objects, lists, arrays, and dictionaries are often allocated on a larger managed memory region.
- Dynamic memory is created when the runtime needs space for values that may change or outlive the current function call.

In many modern languages, allocation is handled automatically by the runtime, which frees the programmer from manually managing memory addresses.

## Deallocation and garbage collection

Deallocation is the process of releasing memory that is no longer needed.

In languages such as JavaScript and Python, the runtime often performs this automatically using garbage collection or reference counting.

### JavaScript / Node.js

Node.js usually runs JavaScript in the V8 engine. V8 performs garbage collection by finding objects that are no longer reachable from active roots and reclaiming them when appropriate.

```js
let order = { item: "tea" };
let altReference = order;

order = null;
altReference = null; // the object can now be reclaimed
```

Setting a variable to `null` removes one reference, but it does not guarantee immediate deletion. The engine decides when it is safe to collect the object.

### Python

CPython uses reference counting as its primary strategy. Each object tracks how many names or references currently point to it. When that count reaches zero, the object can usually be reclaimed immediately.

```python
order = {"item": "tea"}
another_name = order

del order
# the dictionary still exists because another_name references it

del another_name
# now the object can be reclaimed
```

Python also has a cyclic garbage collector for cases where objects reference each other in a loop, which reference counting alone cannot clean up.

## Stack and heap

The terms stack and heap are common when discussing memory, but they are conceptual tools rather than exact universal rules.

- The stack is commonly associated with function call state and local variables.
- The heap is commonly used for dynamically allocated objects and larger data structures.
- The runtime may optimize how values are represented internally.

The important idea is this: memory is allocated as values are created and reclaimed when they are no longer reachable.

## Practical takeaway

A good mental model is:

- Variables provide names for values.
- References determine whether data is still in use.
- Scope defines where a name is valid.
- Reachability determines whether memory can be reused.
- Different runtimes use different mechanisms to reclaim memory.

The exact timing of deallocation is not always predictable, and programs should not rely on an object being deleted at an exact moment in time.

## Summary

Variables are the way programs keep and manipulate data. Memory allocation happens when values are created, and deallocation happens when those values become unreachable or no longer needed. In managed languages like JavaScript and Python, this process is usually automatic, but the underlying approach differs from one runtime to another.

## Learning goals

By understanding this topic, you can better reason about:

- Variable references and aliasing
- Scope and variable lifetime
- Memory reuse and cleanup
- Why garbage collection matters
- How languages manage data behind the scenes

This repository is intended as a learning reference for the relationship between variables, memory allocation, and deallocation in modern runtimes.