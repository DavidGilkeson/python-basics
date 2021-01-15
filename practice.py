# # # Guess the number game

# # import random

# # print("Hello, What is your name")#

# # name = input()

# # secretNumber = random.randint(1,20)

# # print(f"Well {name}, I am thinking of a number between 1 and 20.")

# # # Guess 6 times

# # for guessTaken in range(1, 7):
# #   print("Take a guess")
# #   guess = int(input())
# #   if guess < secretNumber:
# #     print("Your guess is too low.")
# #   elif guess > secretNumber:
# #     print("Your guess is too high")
# #   else:
# #     break # This condition is the right guess
  
# # if guess == secretNumber:
# #   print(f"Good job {name}! You guessed your number in {guessTaken} guesses")
# # else:
# #   print(f"Nope. The number I was thinking of was {secretNumber}")
  
  
# age = 10 
  
# while age < 20:
#     print("I am running" + str(age))
#     age += 1


# n=int(input("enter a number:"))
# list1=[]
# for i in range(n):
#     temp_list=[]
#     for j in range(i+1):
#         if j==0 or j==1:
#             temp_list.append(1)
#         else:
#             temp_list.append(list1[i-1][j-1]+list1[i-1][j]) 
#     list1.append(temp_list)
    
# n=int(input("Enter a number: "))
# list1=[]
# for i in range(n):
#     temp_list=[]
#     for j in range(i+1):
#         if j==0 or j==i:
#             temp_list.append(1)
#         else:
#             temp_list.append(list1[i-1][j-1]+list1[i-1][j]) 
#     list1.append(temp_list)
# print(list1)
# for i in range(n):
#     for j in range(n-i-1):
#         print (format(" ", "<2"), end="")
#     for j in range(i+1):
#         print (format (list1[i][j],"<3") ,end=" ")
#     print()        


# n=int(input("Enter"))
# list1=[]
# for i in range(n):
#     temp_list=[]
#     for j in range(i+1):
#         if j==0 or j==i:
#             temp_list.append(1)
#         else:
#             temp_list.append(list1[i-1][j-1]+list1[i-1][j]) 
#     list1.append(temp_list)
# print(list1)
import pprint

message = "It was a bright cold day in April and the clocks were striking thirteen"
count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1
    
pprint.pprint(count)


