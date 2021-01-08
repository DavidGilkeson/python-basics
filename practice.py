# Guess the number game

import random

print("Hello, What is your name")#

name = input()

secretNumber = random.randint(1,20)

print(f"Well {name}, I am thinking of a number between 1 and 20.")

# Guess 6 times

for guessTaken in range(1, 7):
  print("Take a guess")
  guess = int(input())
  if guess < secretNumber:
    print("Your guess is too low.")
  elif guess > secretNumber:
    print("Your guess is too high")
  else:
    break # This condition is the right guess
  
if guess == secretNumber:
  print(f"Good job {name}! You guessed your number in {guessTaken} guesses")
else:
  print(f"Nope. The number I was thinking of was {secretNumber}")