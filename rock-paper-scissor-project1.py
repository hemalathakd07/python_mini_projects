# rock , paper, scissor

import random

users_choice=int(input("Enter (0/1/2) 0 for rock , 1 for paper, 2 scissor:"))
if(users_choice>2 or users_choice<0):
  print("Entered number is invalid")
else:
  computers_choice=random.randint(0,2)
  print("computer's choice=",computers_choice)
  if users_choice==computers_choice:
    print("It's a draw")
  elif users_choice==0 and computers_choice==2:
    print("You won")
  elif computers_choice==0 and users_choice==2:
    print("You lost")
  elif computers_choice>users_choice:
    print("You lost")
  elif users_choice>computers_choice:
    print("You won")