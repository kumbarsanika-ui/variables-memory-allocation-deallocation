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
