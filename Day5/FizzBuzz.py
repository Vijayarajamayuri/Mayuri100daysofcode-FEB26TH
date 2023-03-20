# # Exercise 4 - FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
for n in range(1,101):
    if n% 15 == 0:
        print("Fizzbuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 ==0:
        print("Fizz")
    else:
       print(n)
