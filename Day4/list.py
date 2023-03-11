# Lists
states_of_america = ["Alabama", "Alaska", "Arizona",  "Arkansas", "California", "Colorado","Connecticut","Wisconsin","Wyoming"]
print(len(states_of_america))
print(states_of_america[1])
# printing -1 == last
print(states_of_america[-1])
states_of_america[1] = "Alaasskka"
print(states_of_america[1])

## append

states_of_america.append("Texas")
print(states_of_america[-1])

## extend

states_of_america.extend(["St loius", "Nebraska"])
print(states_of_america[-1])

# Index Error

#Lists of lists or nested lists

fruits = ["oranges", " Apples", "Bananas ", "Pears "]
veggies = ["SPINACH","KALE","TOMOTOS"]
dirtydozen = [fruits,veggies]
print([fruits,veggies])
# its print of veggies[1] as dirtydozen[1] = b=veggies
print(dirtydozen[1][1])



