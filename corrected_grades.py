# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))
exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]  # Fixed missing commas
total = 0  # Renamed 'sum' to avoid conflict with built-in function 'sum'

for grade in grades:
    total += grade  # Fixed variable name

avg = total / len(grades)  # Fixed 'grdes' typo

# Fixed syntax errors and logic in grading system
if avg >= 90:
    letter_grade = "A"
elif avg >= 80:  # No need to check "avg < 90" as the previous condition already filtered it
    letter_grade = "B"
elif avg >= 70:  # Adjusted the condition to include exactly 70
    letter_grade = "C"
elif avg >= 65:  # Adjusted the range for "D"
    letter_grade = "D"
else:
    letter_grade = "F"

# Displaying grades
for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(avg))
print("Grade: " + letter_grade)

# Fixed conditional check and print statements
if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")
