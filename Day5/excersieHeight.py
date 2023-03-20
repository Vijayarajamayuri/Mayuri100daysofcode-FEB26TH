# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
Total =0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# print(student_heights)
#Write your code below this row 👇
for height in range(0,len(student_heights)):
  Total = Total + int(student_heights[height])
avg= Total/(len(student_heights))
total = student_heights
print(f"Average height is {round(avg)}")




