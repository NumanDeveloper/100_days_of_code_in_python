# Logic
# Take a list of student's marks
# find the max marks

# splitting the input list is vip
student_marks = input("Enter a list of marks: ").split()
max = int(student_marks[0])  # consider first element as max
# typecast the whole list into int
for i in range(0, len(student_marks)):
    # this will typecast each element of the list
    student_marks[i] = int(student_marks[i])

# finding max number using for loop, python max function can also be used here
for i in range(0, len(student_marks)):
    if max < student_marks[i]:
        max = student_marks[i]

print(student_marks)
print(f"Max marks are: {max}")
