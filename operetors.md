# Python Operators and Function Logic

Python operators perform calculations, compare values, combine conditions, and check membership. The task scripts in this folder use these operators to make decisions and return results.

## Common operators used

| Operator | Meaning | Example |
| --- | --- | --- |
| `+`, `-`, `*` | Addition, subtraction, multiplication | `4 + 2` gives `6` |
| `/`, `//`, `%` | Division, floor division, remainder | `7 % 3` gives `1` |
| `**` | Exponentiation | `2 ** 3` gives `8` |
| `&` | Bitwise AND for integers | `7 & 3` gives `3` |
| `==`, `>=` | Equality and greater-than-or-equal comparisons | `score >= 60` |
| `and`, `or`, `not` | Combine or reverse Boolean conditions | `age >= 18 and has_id` |
| `in` | Check whether a value is in a collection | `skill in required_skills` |

## Task 1: Arithmetic calculator

File: `operetors.py`

This script reads two decimal-capable numbers. It always calculates addition, subtraction, and multiplication. Before calculating division, floor division, or remainder, it checks whether the second number is zero. Those three operations are skipped when it is zero because they are undefined for a zero divisor.

## Task 2: Check an integer

File: `task 2.py`

`check_number(number)` uses the remainder operator `%`:

- If `number % 2 == 0`, the number is even; otherwise, it is odd.
- If `number % 3 == 0`, it is divisible by 3.
- If `number % 5 == 0`, it is divisible by 5.

The function returns a tuple containing the parity text and two Boolean results. The script prints each result.

## Task 3: Classify marks

File: `task 3.py`

`get_result(marks)` tests the highest threshold first. Marks of 75 or more return `distinction`; marks from 35 through 74 return `pass`; marks below 35 return `fail`. Checking 75 first ensures distinction marks are not classified as only a pass.

## Task 4: Check student eligibility

File: `task 4.py`

`check_eligibility(marks, attendance, backlog_status)` returns `eligible` only when all three conditions are true:

- Marks are at least 60.
- Attendance is at least 75.
- The backlog status, after trimming spaces and ignoring letter case, is `fail`.

The conditions are joined with `and`, so failing any one condition returns `not eligible`.

## Task 5: Validate a user

File: `task 5.py`

`validate_user(username, password)` returns `valid` only when the username exactly equals `admin` and the password exactly equals `python123`. The `and` operator requires both comparisons to be true. All other combinations return `invalid`.

## Task 6: Calculate a purchase discount

File: `task 6.py`

`calculate_discount(purchase_amount)` chooses one discount rate based on the purchase amount:

- Rs 5,000 or more: 20%.
- Rs 3,000 through Rs 4,999.99: 10%.
- Below Rs 300: 5%.
- Rs 300 through less than Rs 3,000: no discount, because no rate was specified for this range.

It multiplies the purchase amount by the selected rate, subtracts the discount from the purchase amount, and returns both amounts as a tuple.

## Task 7: Check access

File: `task 7.py`

`check_access(age, has_id, is_employee)` grants access when the person is at least 18 and has an ID, or when the person is an employee. The parentheses group the age-and-ID requirements; the `or` means employee status can grant access independently. Otherwise, it returns `access denied`.

## Task 8: Check a required skill

File: `task 8.py`

The `required_skills` list contains `python`, `SQL`, `git`, and `HTML`. `check_skill(skill_name)` uses `in` to look for an exact match in that list. It returns `skill available` for a match and `skill not available` otherwise. Matching is case-sensitive.

## Task 9: Calculate with a selected operator

File: `task 9.py`

`calculate(a, operator, c)` first checks that the operator is one of `+`, `-`, `*`, `%`, `/`, `//`, `&`, or `**`. An unsupported operator returns `Invalid operator`. For `%`, `/`, and `//`, it also checks that `c` is not zero; otherwise, it returns `Cannot divide by zero`. If the checks pass, it performs the requested operation and returns the result. The script reads integers so the bitwise AND operator `&` can be used.

## Task 10: Determine placement results

File: `task 10.py`

`determine_placement(age, marks, attendance, experience, has_backlogs)` returns three values:

- Placement status is `eligible` when marks are at least 60, attendance is at least 75, and the student has no backlogs. Otherwise, it is `not eligible`.
- Marks category is `distinction` when marks are at least 75 and the student has no backlogs. Otherwise, it is `standard`.
- Experience category is `fresher` when experience is zero; otherwise, it is `experienced`.

The function accepts `age`, but the task does not specify an age rule, so age does not currently affect any result.
