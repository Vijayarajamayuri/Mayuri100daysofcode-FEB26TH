# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# bmi= float(weight) % (float(height)* float(height))
h= float(height)
w= float(weight)
bmi= w / (h ** 2) 
print(int(bmi))
