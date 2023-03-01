# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height * height)
# print(bmi)

# Method 1
# if  bmi < 35:
#     # Nested if statement
#     if bmi > 30:
#         print(f"Your bmi is {bmi} they are obese")

#         # else if statement 
#     elif 25 <bmi < 30:
#         print(f"Your bmi is {bmi} they are slightly overweight")
#     elif 18.5 <bmi < 25:
#         print("they have a normal weight")
#     else:
#         print("they are underweight")   
# # Above 35 they are clinically obese.
# else:
#     print("they are clinically obese.")


if bmi <18.5:
    print("underweight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("slight ow")     
elif bmi < 35:
    print("obese")
else:
    print("clinically obese") 

# Method 3
# if  bmi > 18.5:
#     print("they have a normal weight")
#     # Nested if statement
#     if bmi > 25:
#         print("they are slightly overweight")

#         # else if statement 
#     elif 35 > bmi > 30:
#         print("they are obese")

#     else:
#         print("they are clinically obese.")    
# else:
#     print("they are underweight")