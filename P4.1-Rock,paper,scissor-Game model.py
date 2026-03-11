# It is a demo code to the rock paper scissor Game-Model 

import random

print(" Welcome to the rock , paper , scissor game ")

print(" Choose any one given below ")
print("0.Rock")
print("1.Paper")
print("2.Scissor")

options=["rock","paper","scissor"]
print("Enter 0 for rock , 1 for paper , 2 for scissor ")
n=int(input("Enter your Choice : "))
print(f"Your choice = {options[n]}")

print("Computer Choice")
p=random.randint(0,2)
print(f"Computer choice= {options[p]}")

if n==p:
    print("Draw")
elif n==0 and p==1:
    print("You lose!")
elif n==0 and p==2:
    print("You win!")
elif n==1 and p==0:
    print("You win!")
elif n==1 and p==2:
    print("You lose!")
elif n==2 and p==0:
    print("You lose!")
elif n==2 and p==1:
    print("You win!")
else:
    print(" Invalid Choice! Please choose correct option ")
