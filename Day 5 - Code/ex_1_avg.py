# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights: ").split()
# converting data type of all the list elements into int
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
sum = count = 0

for i in range(0, len(student_heights)):
    sum += student_heights[i]
    count += 1

avg = round(sum/count)
print(student_heights)
print(f"Average: {avg}")
