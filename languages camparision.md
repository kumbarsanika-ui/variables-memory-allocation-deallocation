# JavaScript, Node.js, Python, and Java: Variables and Memory

This guide compares how the four environments handle variables, objects, functions, memory, and execution. JavaScript is a programming language. Node.js is a runtime that executes JavaScript outside a browser, using the V8 engine plus Node APIs and other runtime components. Browser JavaScript uses the browser's runtime APIs instead.

## 1. Variable declaration

| Environment | How a name is introduced |
| --- | --- |
| JavaScript | `let` and `const` declare block-scoped bindings. Older `var` is function-scoped (or global-scoped at top level) and has different hoisting behavior. |
| Node.js | Uses JavaScript's `let`, `const`, and `var`; Node adds runtime APIs, not a new variable syntax. |
| Python | Assignment binds a name to an object. A declaration keyword is not required. |
| Java | A local variable is declared with a type, such as `int count = 3;`. `var` can infer a local variable's static type in supported Java versions, but Java remains statically typed. |

`const` prevents a JavaScript binding from being reassigned; it does not make an object immutable. Python type annotations can document or help tools check expected types, but Python does not enforce them by default at runtime.

## 2. Static and dynamic typing

Java is statically typed: the compiler checks types and many type errors before a program runs. A Java variable has a declared or inferred type, and that type does not change during execution. Java still chooses overridden methods dynamically at runtime; static typing does not mean every behavior is decided at compile time.

JavaScript and Python are dynamically typed: the value has a type at runtime, and a name can be rebound to a value of another type. Errors such as adding incompatible values may therefore appear when that code executes. JavaScript engines and Python tools can perform optimizations or optional checks, but this does not change their core dynamic typing model.

## 3. Primitive, reference, and object types

JavaScript has primitive values such as numbers, strings, booleans, `null`, `undefined`, `bigint`, and symbols. Objects include arrays and functions. Primitive assignment copies the value; assigning an object copies its reference value.

Python represents values as objects, including integers, strings, lists, and functions. Names refer to those objects; mutability is a property of the object's type, not a distinction between primitive and object values.

Java separates primitive types (`int`, `double`, `boolean`, and others) from reference types (classes, arrays, and interfaces). A reference variable can refer to an object or contain `null`. Java `String` values are objects even though strings are commonly used like simple values.

## 4. Names, objects, references, and assignment

Assignment does not always copy an object. For example, in JavaScript, Python, and Java:

```python
a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3]
```

Both names refer to the same list, so changing the list through `b` is visible through `a`. The assignment copied or created another reference to that list; it did not copy the list itself. Rebinding `b` to a different list would not rebind `a`.

Java follows the same idea for object references: `b = a` copies the reference, not the object. For primitives, such as `int`, assignment copies the value. To copy a collection, use an intentional copy operation; decide whether a shallow copy (new outer collection, shared nested objects) or a deep copy (nested objects copied too) is needed.

## 5. Mutable and immutable values

An immutable object's value cannot be changed after creation. A mutable object's state can be changed while it remains the same object.

| Environment | Immutable examples | Mutable examples |
| --- | --- | --- |
| JavaScript / Node.js | Strings, numbers, booleans | Arrays and ordinary objects |
| Python | Strings, integers, tuples (the tuple structure) | Lists, dictionaries, sets |
| Java | `String`, wrapper objects such as `Integer` | Arrays and mutable collections such as `ArrayList` |

For example, `text = text + "!"` creates a new string value rather than modifying the original string in place. By contrast, appending to a JavaScript array, Python list, or Java `ArrayList` changes that collection. An immutable container can still refer to a mutable object: a Python tuple may contain a list whose contents can change.

## 6. Stack and heap memory

The call stack tracks active function or method calls. It typically contains call-frame information such as return locations, parameters, and local execution state. The heap is commonly used for dynamically allocated objects whose lifetime is not limited to one call.

The phrase "variables are on the stack and objects are on the heap" is only a teaching model, not a language guarantee. A local variable may be held in a CPU register, optimized away, or represented in another way. A local reference can point to a heap object. Compilers and runtimes can optimize allocations, and implementation details differ among V8, CPython, and JVM implementations.

Think in terms of behavior and reachability first; do not rely on a source-level variable having a particular physical memory address or location.

## 7. What happens during a function or method call?

When a function is called, the runtime establishes execution state for that call, supplies its arguments as parameters, and begins executing its body. Local names belong to that call's scope. A return statement supplies a result to the caller and ends that invocation; local names stop being accessible from outside their scope.

Calls are usually tracked with a call stack. If one function calls another, the second call becomes active while the first waits. Deep or unbounded recursion can exhaust the available call stack. Returning a reference to an object can keep that object alive after the function returns, even though the function's local name is gone.

## 8. Functions across the four environments

JavaScript and Python functions are first-class values: they can be assigned to names, passed as arguments, returned from other functions, and stored in collections. Node.js uses the same JavaScript function behavior.

In Java, a method belongs to a class or object; a method name by itself is not generally passed around as a value. Java supports lambdas and method references, which can be used where a functional interface is expected. A functional interface has one abstract method, such as `Runnable` or `Function<T, R>`, and provides a typed way to use behavior as a value.

## 9. Pass by value and reference semantics

Pass-by-value means a function receives a copy of an argument value. Pass-by-reference, in the strict sense, would let the function directly rebind the caller's variable. JavaScript, Python, and Java use pass-by-value for function arguments. When the value is a reference to an object, the copied value refers to the same object; this is often called pass-by-sharing.

```python
def change(items):
	items.append("new")  # Mutates the shared list

def rebind(items):
	items = ["different"]  # Rebinds only the local parameter

values = ["original"]
change(values)
print(values)  # ["original", "new"]
rebind(values)
print(values)  # Still ["original", "new"]
```

The same distinction applies to JavaScript arrays/objects and Java objects/arrays. A function can mutate a shared object and the caller can observe that mutation. Assigning a new object to the function's parameter does not replace the caller's variable. Python describes this model as passing object references by assignment; Java and JavaScript still pass the reference value by value.

## 10. Closures

A closure is a function together with access to names from its surrounding lexical scope. In JavaScript and Python, an inner function can use a variable from an outer function. If the inner function is returned or stored, it can continue using the captured environment after the outer call has finished.

```python
def make_counter():
	count = 0

	def next_value():
		nonlocal count
		count += 1
		return count

	return next_value
```

The returned function keeps access to `count`, so the relevant captured state must remain available. Java lambdas can capture local variables only when they are final or effectively final. A captured object reference may still refer to a mutable object; the restriction is on reassignment of the captured local variable, not necessarily on mutation of the object.

Closures can extend the lifetime of captured data. They are useful for callbacks and state, but can also retain large objects longer than intended.

## 11. Garbage collection

Garbage collection reclaims memory used by objects that a program can no longer reach. It reduces the need for programmers to explicitly free every object and helps prevent many use-after-free and double-free errors.

An object generally becomes eligible for collection when it is no longer reachable from live program roots, such as active calls, global or static state, and retained callbacks. Eligibility does not mean memory is released immediately; the runtime decides when to collect and how to reuse or return memory.

JavaScript's `delete` removes an object's property; it is not a command to free the property's former value immediately. Python's `del` removes a name, item, or attribute; it does not promise immediate release of memory to the operating system. If other references remain, the object stays alive. Even after an object is reclaimed, a runtime allocator may keep the memory available for reuse rather than returning it to the OS at once.

## 12. Garbage collection comparison

- **JavaScript and Node.js:** V8 uses a tracing garbage collector. It finds objects reachable from roots and can collect unreachable objects. Collection strategies and timing are runtime-managed and may change between V8 versions.
- **CPython:** Common CPython builds use reference counting, which can reclaim many objects when their reference count reaches zero, plus a cyclic garbage collector for some unreachable reference cycles. Other Python implementations may manage memory differently.
- **Java:** JVMs use tracing garbage collectors. The JVM provides different collectors and configurations with tradeoffs in throughput, pause time, and memory use.

None of these models guarantees that an object will be collected at the exact moment it becomes unreachable.

## 13. Memory leaks despite garbage collection

Garbage collection cannot reclaim an object that is still reachable, even if the program no longer needs it. This is a logical memory leak: the program accidentally retains references.

Common causes include unbounded caches, global variables holding old data, long-lived collections that are never cleared, callbacks retaining large objects, and event listeners that are not removed. In Node.js or browser JavaScript, an event source can keep a listener alive; in Python or Java, long-lived registries and caches can retain objects in the same way. Clear or bound caches, unregister listeners, and inspect object-retention paths when memory grows unexpectedly.

## 14. Runtime comparison

- **JavaScript:** The language is standardized, but the host supplies APIs. A browser typically runs JavaScript in a browser engine with browser APIs.
- **Node.js:** Executes JavaScript using V8 and supplies server-side APIs such as file access, networking, and process management. Its event loop and supporting runtime components handle asynchronous work.
- **Python:** Python is a language with multiple implementations. CPython is the most widely used implementation and includes its own bytecode virtual machine and runtime services.
- **Java:** Java source is compiled to class-file bytecode and executed by a Java Virtual Machine (JVM), which provides runtime services such as class loading, memory management, and garbage collection.

The language specifies observable behavior; details such as object layout, garbage collector strategy, and optimization depend on the runtime and its version.

## 15. Compilation, interpretation, and JIT compilation

These categories overlap, so "compiled versus interpreted" is an oversimplification.

- **JavaScript on V8:** V8 parses source, may produce internal bytecode, and can interpret or compile frequently executed code to optimized machine code. The exact pipeline is an engine implementation detail.
- **CPython:** CPython compiles source to Python bytecode and executes it on its virtual machine. It may cache bytecode in `__pycache__`; standard CPython does not normally JIT-compile application code to machine code. Other Python implementations may use different strategies.
- **Java:** `javac` compiles source to JVM bytecode. The JVM can interpret bytecode and JIT-compile frequently executed portions to machine code while the program runs.

Compilation can happen before execution, during execution, or in multiple stages. It does not by itself tell you how fast a program will be; runtime optimization, workload, libraries, and I/O also matter.

## 16. Event loops, asynchronous I/O, and threads

Node.js commonly runs JavaScript callbacks on an event loop. Asynchronous I/O lets the program start an operation and process other work while waiting for the result. Some tasks use runtime or operating-system thread pools, and Node.js also offers worker threads for CPU-intensive work. A long CPU-bound callback can block the event loop and delay unrelated requests.

Python's `asyncio` provides an event loop and `async`/`await` for cooperative I/O concurrency. Threads can be useful for blocking I/O; CPU-bound parallel execution depends on the Python implementation and build. In common CPython builds, the Global Interpreter Lock (GIL) limits simultaneous execution of Python bytecode by threads, though processes, native code, and optional free-threaded builds have different behavior.

Java supports threads, executors, and (in modern Java releases) virtual threads. I/O-bound tasks spend time waiting, while CPU-bound tasks spend time computing. Choose concurrency tools for the workload: asynchronous I/O can handle many waits efficiently, while CPU-heavy work usually needs parallel computation or offloading.

## 17. A typical HTTP request flow

```text
HTTP request
	-> server or framework receives and parses it
	-> route handler validates input
	-> functions/methods use local names and objects
	-> application calls a database or another API
	-> result is transformed and serialized
	-> HTTP response is sent
```

The handler's local variables belong to that invocation. Objects may be created for the request, shared with other code, or retained in application-wide caches. Database and network calls may wait asynchronously or occupy a thread, depending on the runtime and libraries. Errors and timeouts must also be converted into appropriate responses.

## 18. Comparing performance

Avoid asking which language is simply "the fastest." Performance depends on the workload, algorithm, data structures, CPU use, I/O wait, memory use, garbage collection, runtime warm-up, libraries, and deployment architecture.

For a database-backed service, query time and network latency may dominate language execution time. For numerical computation, optimized native libraries may matter more than the surrounding language. Measure a representative workload, profile its bottlenecks, and optimize the largest cost first.

## 19. Variable lifetime and object lifetime

A variable or binding exists within its scope and program execution rules. A local name normally stops being accessible when its function call returns. A global or module-level name may remain available for the life of the process.

An object's lifetime is different. An object can remain reachable after the function that created it returns if another name, collection, closure, cache, or callback refers to it. Once it is unreachable, it may become eligible for garbage collection; the runtime determines when memory is reclaimed or reused. Therefore, the lifetime of a name, the lifetime of an object, and the time memory is returned to the operating system are three different things.

## 20. What happens when `result = a + b` runs?

At a high level, the runtime evaluates the expression on the right, obtains the current values referred to by `a` and `b`, performs the language's addition operation, and binds or assigns the result to `result`. The physical implementation can use registers, stack slots, heap objects, or optimizations; the source line alone does not specify that layout.

### Python

```python
result = a + b
```

Python looks up the objects bound to `a` and `b`, applies the addition protocol for their types (which can involve `__add__`), and binds the resulting object to `result`. For integers this computes a numeric sum; for strings, `+` concatenates strings. Unsupported combinations raise an exception at runtime.

### JavaScript and Node.js

```javascript
const result = a + b;
```

Node.js uses JavaScript's `+` semantics. The operator can add numbers or concatenate strings; JavaScript converts values according to its coercion rules, so mixed types may produce surprising results. `const` means the `result` binding cannot be reassigned, but if the result is an object, that object's contents may still be mutable.

### Java

```java
int result = a + b;
```

The compiler checks the operand and result types. With `int` operands, Java performs integer addition and stores the result in an `int`; overflow wraps according to Java's integer rules. If the operands are reference types or another numeric type, the allowed operation and conversions depend on their declared types. Type errors are generally reported at compile time.

In all three examples, assignment binds or stores a result; whether that result is a primitive value, an immutable object, or a reference depends on the language and operand types.