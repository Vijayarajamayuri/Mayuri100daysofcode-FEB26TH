#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill= input("Enter the total bill: $")
No= input("eNTER NO OF PEOPLE: ")
Tip= input("Enter the tip between 10,12,15")
total= float(bill)
NUM= int(No)
tip= int(Tip)
# type(bill)
# print(type(bill)) is string 
Split= ((total / NUM ) * (1+ tip / 100))
print(f"Each person should pay ${round(Split,2)}")

