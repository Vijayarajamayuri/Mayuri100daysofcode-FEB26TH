# HEIGHT CHECK#######################
print("welcome to rollercostter")
height = int(input("Enter the height in cm: "))
age = int(input("Enter your age: "))
if height >= 120:
    print("You can ride the rollercoster")
    # Nested if statement
    if age >= 18:
        print("Please pay $7")
    elif age < 12:
        print("Please pay $3")

    else:
        print("Please pay $5")    
else:
    print("You cannt ride the rollercoster")   