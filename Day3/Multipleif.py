# HEIGHT CHECK#######################

# Multiple if checks all if statements 
print("welcome to rollercostter")
height = int(input("Enter the height in cm: "))
age = int(input("Enter your age: "))
bill= 0

if height >= 120:
    print("You can ride the rollercoster")
    # Nested if statement
    if age >= 18 and age < 45:
        bill= 7
        print("Your eligible for  pay $7")

        # else if statement 
    elif age < 12:
        bill=3
        print("Your eligible for  pay $3")
    elif age < 55 and age > 45:
        bill =0
        print("You ride for free ")
    else:
        bill=5
        print("Your eligible for  pay $5")  
    wants_photo= input("Do you want photo? Y or N ")
    if wants_photo== "Y":
        # Add $3 for photo
        bill = bill + 3;
        print(f"You have to pay ${bill}")

        



else:
    print("You cannt ride the rollercoster")   


    