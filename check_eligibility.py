def check_eligibility(marks, attendance, backlog_status):
	if marks >= 60 and attendance >= 75 and backlog_status.strip().lower() == "fail":
		return "eligible"
	return "not eligible"


marks = float(input("Enter the student's marks: "))
attendance = float(input("Enter the student's attendance percentage: "))
backlog_status = input("Enter the backlog status (pass/fail): ")

print(check_eligibility(marks, attendance, backlog_status))
