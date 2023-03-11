# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
# what do you choose ? Type 0= rock 1= paper 2=scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
plays = [rock,paper,scissors]
play = input("what do you choose ? Type 0= rock 1= paper 2=scissors : ")
your_choice = int(play)
computer = random.randint(0,2)
# This doesnt work for input > 2
# Need to move it to your choice to int()
print(f"You choose: \n  {plays[your_choice]}")
print(f"Computer choose: \n {plays[computer]}")

if your_choice == 0 and computer == 2:
    print("You Win!")

elif computer > your_choice:
    print("You lose")


elif your_choice == computer:
    print("DRaw")
else:
    print("You typed invalid number")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
