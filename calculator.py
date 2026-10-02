first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)

if second_number == 0:
	print("Division, floor division, and remainder are undefined when dividing by zero.")
else:
	print("Division:", first_number / second_number)
	print("Floor division:", first_number // second_number)
	print("Remainder:", first_number % second_number)

