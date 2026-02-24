# password generator

import random

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M',
         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
         'a','b','c','d','e','f','g','h','i','j','k','l','m',
         'n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers=[0,1,2,3,4,5,6,7,8,9] # convert this into string later 

symbols=['!','@','#','$','%','^','&','*','(',')','+','_','-','/']

n_letters=int(input("Enter the number of letters to be there in your password:"))
n_numbers=int(input("Enter the number of numbers to be there in your password:"))
n_symbols=int(input("Enter the number of symbols to be there in your password:"))

password=""

for i in range(1,n_letters+1):
  char=random.choice(letters)
  password+=char

print(password)

for i in range(1,n_numbers+1):
  char=str(random.choice(numbers))
  password+=char

print(password)

for i in range(1,n_symbols+1):
  char=random.choice(symbols)
  password+=char

print(password)

print("The final generated password is",password)