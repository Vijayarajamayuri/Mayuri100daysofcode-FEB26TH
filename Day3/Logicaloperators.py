# logical operators 
# # AND OR NOT 
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
Name1 = input("What is your name? \n")
Name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = Name1.lower()
name2 = Name2.lower()

# t_count = name1.count("t") +  name2.count("t")
# r_count = name1.count("r") or name2.count("r")
# u_count = name1.count("u") or name2.count("u")
# e_count = name1.count("e") or name2.count("e")
# L_count = name1.count("l") or name2.count("l")
# O_count = name1.count("o") or name2.count("o")
# V_count = name1.count("v") or name2.count("v")
# E_count = name1.count("e") or name2.count("e")
t_count = name1.count("t") +  name2.count("t")
r_count = name1.count("r") + name2.count("r")
u_count = name1.count("u") + name2.count("u")
e_count = name1.count("e") + name2.count("e")
L_count = name1.count("l") + name2.count("l")
O_count = name1.count("o") + name2.count("o")
V_count = name1.count("v") + name2.count("v")
E_count = name1.count("e") + name2.count("e")
true = t_count+ r_count+u_count+e_count
love = L_count+O_count+V_count+E_count
print(f"{true}{love}")
print(love)
print(true)

# Method 2 


total = name1.lower() + name2.lower()
t = total.count("t")
r = total.count("r")
u = total.count("u")
e = total.count("e")
true = t+r+ u + e
l =total.count("l")
o =total.count("o")
v=total.count("v")
e =total.count("e")
love = l+o+v+e


print(love)
print(true)
