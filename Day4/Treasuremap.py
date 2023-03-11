# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜x️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# positions is string print(type(position))
Horizonal= int(position[0]) #2
# 23
vertical= int(position[1]) #3

r=map[vertical-1]
r[Horizonal-1] = "X"



# map[r(Horizonal-1)]
# print(r[Horizonal-1])
# horizontal

#if map

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
