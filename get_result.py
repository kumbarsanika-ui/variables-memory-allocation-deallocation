def get_result(marks):
	if marks >= 75:
		return "distinction"
	if marks >= 35:
		return "pass"
	return "fail"


marks = float(input("Enter the student's marks: "))
print(get_result(marks))
