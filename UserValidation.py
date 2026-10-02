def calculate(a, operator, c):
	if operator not in ("+", "-", "*", "%", "/", "//", "&", "**"):
		return "Invalid operator"

	if operator in ("%", "/", "//") and c == 0:
		return "Cannot divide by zero"

	if operator == "+":
		return a + c
	if operator == "-":
		return a - c
	if operator == "*":
		return a * c
	if operator == "%":
		return a % c
	if operator == "/":
		return a / c
	if operator == "//":
		return a // c
	if operator == "&":
		return a & c
	return a ** c


first_number = int(input("Enter the first integer: "))
operator = input("Enter an operator (+, -, *, %, /, //, &, **): ")
second_number = int(input("Enter the second integer: "))

print(calculate(first_number, operator, second_number))
