def determine_placement(age, marks, attendance, experience, has_backlogs):
	placement_eligible = marks >= 60 and attendance >= 75 and not has_backlogs

	if marks >= 75 and not has_backlogs:
		marks_category = "distinction"
	else:
		marks_category = "standard"

	if experience == 0:
		experience_category = "fresher"
	else:
		experience_category = "experienced"

	placement_status = "eligible" if placement_eligible else "not eligible"
	return placement_status, marks_category, experience_category


age = int(input("Enter the student's age: "))
marks = float(input("Enter the student's marks: "))
attendance = float(input("Enter the student's attendance percentage: "))
experience = float(input("Enter the student's years of experience: "))
has_backlogs = input("Does the student have backlogs? (yes/no): ").strip().lower() == "yes"

placement_status, marks_category, experience_category = determine_placement(
	age, marks, attendance, experience, has_backlogs
)

print("Placement status:", placement_status)
print("Marks category:", marks_category)
print("Experience category:", experience_category)
