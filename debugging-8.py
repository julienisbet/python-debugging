# this is a random guessing game
# the user should guess a number between 1 and 10
# the game ends once they guess the correct number
# fix the program which currently has an error

import random

active = True
answer = random.randint(1, 10)
while active:
  num = int(input("Please guess a number between 1 and 10\n"))
  if num = answer:
    active = False
    print("You win!")
    print(f"The number was {num}")
  else:
    print("Please guess again!")
