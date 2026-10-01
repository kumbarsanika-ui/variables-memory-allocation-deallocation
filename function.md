# Python Functions

## 1. Why use functions?

Without a function, the same work may need to be repeated:

```python
print("Welcome, Sanika")
print("Welcome, S_K")
print("Welcome, S_K_K")
```

`break` is not needed between these statements. In Python, `break` is used inside a loop to exit that loop.

A function lets us write the behavior once and reuse it with different inputs:

```python
def welcome(name):
	print("Welcome,", name)


welcome("Sanika")
welcome("S_K")
welcome("S_K_K")
```

Functions help with code reuse, reduce repetition, improve organization, and make code easier to maintain and test.

## 2. What is a function?

A function is a reusable, named block of code that performs a task. It can accept inputs and can return a result.

```python
def add(a, b):
	return a + b


result = add(2, 3)
print(result)  # 5
```

## 3. Defining versus calling a function

Defining a function creates it; the body does not run until the function is called.

```python
def greet():
	print("Hello")


greet()  # Calls the function and runs its body.
```

## 4. A function without parameters

```python
def welcome_to_lab():
	print("Welcome to Nighan2 Labs")


welcome_to_lab()
```

Use a function without parameters when it does not need input from its caller.

## 5. A function with a parameter

```python
def welcome(name):
	print("Welcome,", name)


welcome("Sanika")
```

Here, `name` is a **parameter** in the function definition. `"Sanika"` is an **argument** passed to the function call.

## 6. Multiple parameters

```python
def add(a, b):
	return a + b


print(add(10, 20))  # 30
```

The function has two parameters, `a` and `b`; the call supplies two arguments, `10` and `20`.

## 7. `print()` versus `return`

`print()` displays a value. `return` sends a value back to the caller so the program can use it.

```python
def add_and_print(a, b):
	print(a + b)


def add_and_return(a, b):
	return a + b


add_and_print(10, 20)  # Displays 30
result = add_and_return(10, 20)
print(result)  # Displays 30
```

Returning a value is useful when the result needs to be stored, combined with other calculations, or passed to another function.

## 8. What happens after `return`?

`return` immediately ends that function call. Statements later in the same function call are not executed.

```python
def test():
	return 10
	print("This line does not run")


print(test())  # 10
```

Code after the call to `test()` can still run; `return` only exits the function.

## 9. Returning multiple values

Python can return several values, which are packed into a tuple and can be unpacked by the caller.

```python
def calculate(a, b):
	return a + b, a - b, a * b


sum_result, difference, product = calculate(10, 5)
print(sum_result)  # 15
print(difference)  # 5
print(product)  # 50
```

## 10. Default parameters

A default parameter value is used when the caller does not provide that argument.

```python
def greet(name="Sanika"):
	print("Hello,", name)


greet()         # Hello, Sanika
greet("Aishu")  # Hello, Aishu
```

Default parameters are useful when a common value is appropriate most of the time, while still allowing callers to provide a different value.

## 11. Positional arguments

Positional arguments are matched to parameters by their order.

```python
def student(name, age):
	print(name, age)


student("Sanika", 21)
```

`"Sanika"` is passed to `name`, and `21` is passed to `age`.

## 12. Keyword arguments

Keyword arguments identify the parameter by name, so their order can vary.

```python
def student(name, age):
	print(name, age)


student(age=21, name="Sanika")
```

## 13. Combining positional and keyword arguments

Positional arguments can be followed by keyword arguments. A positional argument cannot follow a keyword argument in the same call.

```python
def student(name, age, course):
	print(name, age, course)


student("Sanika", 21, course="BCA")  # Valid
student(name="Sanika", age=21, course="BCA")  # Also valid
```

For example, `student(name="Sanika", 21, course="BCA")` is invalid because a positional argument follows a keyword argument.

## 14. `*args`

Use `*args` when a function should accept any number of positional arguments. Inside the function, `args` is a tuple.

```python
def add(*numbers):
	total = 0
	for number in numbers:
		total += number
	return total


print(add(10, 20))  # 30
print(add(10, 20, 30))  # 60
print(add(1, 2, 3, 4, 5))  # 15
```

The name `args` is a convention; the `*` is what gathers the extra positional arguments.

## 15. `**kwargs`

Use `**kwargs` when a function should accept any number of keyword arguments. Inside the function, `kwargs` is a dictionary.

```python
def show_student(**details):
	print(details)


show_student(name="Sanika", age=21, course="BCA")
# {'name': 'Sanika', 'age': 21, 'course': 'BCA'}
```

The name `kwargs` is a convention; the `**` gathers the extra keyword arguments.

## 16. Combining parameters, `*args`, and `**kwargs`

A function can combine regular parameters, extra positional arguments, and extra keyword arguments. A common order is regular parameters, `*args`, then `**kwargs`.

```python
def example(a, b=10, *args, **kwargs):
	print("a:", a)
	print("b:", b)
	print("extra positional arguments:", args)
	print("extra keyword arguments:", kwargs)


example(1, 2, 3, 4, color="blue")
```

Here, `a` is `1`, `b` is `2`, `args` is `(3, 4)`, and `kwargs` is `{"color": "blue"}`.

## 17. Local and global scope

A variable created inside a function is local to that function. A function can read a name defined in the global scope if that name is available.

```python
def show_local():
	message = "local"
	print(message)


show_local()

message = "global"


def show_global():
	print(message)


show_global()
```

## 18. The `global` keyword

Use `global` to reassign a module-level variable from inside a function.

```python
count = 0


def increment():
	global count
	count += 1


increment()
print(count)  # 1
```

Avoid unnecessary global state. Passing values as parameters and returning results usually makes functions easier to reuse and test.

## 19. A local variable is not available outside its function

```python
def make_value():
	value = 10


make_value()
print(value)  # Raises NameError: value is local to make_value().
```

To use the value outside the function, return it:

```python
def make_value():
	value = 10
	return value


result = make_value()
print(result)  # 10
```

## 20. Functions can call other functions

Breaking work into functions lets one function use another function's result.

```python
def add(a, b):
	return a + b


def display_result():
	result = add(10, 20)
	print(result)


display_result()  # 30
```

A larger program might follow a flow like:

```text
main() -> validate() -> calculate() -> save() -> display()
```


## 21. Function calling flow

When a function is called, Python matches the arguments to the parameters, runs the function body, and sends its return value back to the caller.

```python
def multiply(a, b):
	return a * b


result = multiply(5, 4)
print(result)  # 20
```

Python calls `multiply` with `a = 5` and `b = 4`. The function calculates `5 * 4` and returns `20`; then that value is assigned to `result`.

## 22. Functions are objects

Functions are objects in Python. A variable can refer to a function, and calling that variable calls the function.

```python
def greet():
	print("Hello")


x = greet  # Assign the function object; do not call it yet.
x()        # Calls greet() and prints Hello.
```

Here, `x` refers to the same function object as `greet`.

## 23. Passing a function to another function

Because functions are objects, they can be passed as arguments. A function that accepts or returns another function is called a **higher-order function**.

```python
def square(x):
	return x * x


def process(function, value):
	return function(value)


print(process(square, 5))  # 25
```

`process` receives `square` as its `function` argument and calls it with `5`.

## 24. Lambda functions

A `lambda` creates a small anonymous function expression. It can contain one expression and returns that expression's result.

```python
square = lambda x: x * x
print(square(5))  # 25
```

Lambdas are often useful for short operations passed to other functions:

```python
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)  # [2, 4, 6, 8]
```

For more complex logic, use a named function instead; it is easier to read and reuse.

## 25. Recursion

A recursive function calls itself. It needs a **base case** that stops the recursion.

```python
def countdown(n):
	if n == 0:
		return
	print(n)
	countdown(n - 1)


countdown(5)  # Prints 5, 4, 3, 2, 1.
```

When `n` reaches `0`, the base case returns and the calls finish. Without a base case, recursion continues until Python raises a `RecursionError`.

## 26. Function documentation

A **docstring** is a string at the beginning of a function body that describes the function. It is available through the function's `__doc__` attribute.

```python
def add(a, b):
	"""Return the sum of two numbers."""
	return a + b


print(add.__doc__)
```

Writing clear docstrings is a useful professional Python habit, especially when a function's purpose or inputs are not obvious.

## 27. Type hints

Type hints communicate intended types to developers and tools. Python generally does not enforce them automatically at runtime.

```python
def add(a: int, b: int) -> int:
	return a + b
```

Here, the hints indicate that `a` and `b` are expected to be integers and that the function is expected to return an integer.

## 28. Practical example: electricity bill

This example charges 2 units per kWh for the first 100 units, 4 for the next 100, and 6 for any units above 200, plus a fixed charge of 100.

```python
def calculate_bill(units):
	if units <= 100:
		amount = units * 2
	elif units <= 200:
		amount = 100 * 2 + (units - 100) * 4
	else:
		amount = 100 * 2 + 100 * 4 + (units - 200) * 6
	return amount + 100


units = int(input("Enter units: "))
bill = calculate_bill(units)
print("Bill:", bill)
```

Putting the calculation in `calculate_bill` separates the billing logic from input and output. This makes the calculation reusable, easier to test, easier to read, and easier to maintain.

## 29. Function design

A well-designed function usually has a clear input, performs a focused piece of processing, and produces an output. Some functions perform an action, such as displaying information, instead of returning a value.

## 30. Avoid giant functions

A function that handles input, validation, calculations, database work, and printing all at once is difficult to understand and test. Split those responsibilities into smaller functions instead:

```python
def get_student():
	pass


def validate_student(student):
	pass


def calculate_student_result(student):
	pass


def save_student(student):
	pass


def display_student(student):
	pass
```

These are function-only examples; you do not need to create a class to organize code this way. Give each function one clear responsibility. Smaller, focused functions are generally easier to read, test, reuse, and maintain.