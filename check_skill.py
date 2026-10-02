required_skills = ["python", "SQL", "git", "HTML"]


def check_skill(skill_name):
	if skill_name in required_skills:
		return "skill available"
	return "skill not available"


skill_name = input("Enter a skill name: ")
print(check_skill(skill_name))
