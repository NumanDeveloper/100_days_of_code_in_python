student_scores = {
    "Ahmer": 81,
    "Imran": 78,
    "Numan": 99,
    "Hasnain": 74,
    "Mubashir": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Accesptable"
    else:
        student_grades[student] = "Fail"
# 🚨 Don't change the code below 👇
print(student_grades)
