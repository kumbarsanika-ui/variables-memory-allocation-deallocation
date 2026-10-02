def check_number(number):
	parity = "even" if number % 2 == 0 else "odd"
	divisible_by_3 = number % 3 == 0
	divisible_by_5 = number % 5 == 0
	return parity, divisible_by_3, divisible_by_5


number = int(input("Enter an integer: "))
parity, divisible_by_3, divisible_by_5 = check_number(number)

print("The number is", parity)
print("Divisible by 3:", divisible_by_3)
print("Divisible by 5:", divisible_by_5)
