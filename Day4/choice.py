# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
s = len(names)

print(names)
print(f" {names[random.randint(0,s-1)]} will pay bill")

print()
# print(random.randint(choice))
# print(total)
# names_list = [names]
# print(random.choice(names))
