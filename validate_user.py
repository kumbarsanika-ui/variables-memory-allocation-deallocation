def validate_user(username, password):
	if username == "admin" and password == "python123":
		return "valid"
	return "invalid"


username = input("Enter the username: ")
password = input("Enter the password: ")

print(validate_user(username, password))
