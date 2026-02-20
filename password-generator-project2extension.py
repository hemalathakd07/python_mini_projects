import random

# password generator

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M',
         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
         'a','b','c','d','e','f','g','h','i','j','k','l','m',
         'n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','+','_','-','/']

n_letters=int(input("how many letters do you want in your password?"))
n_symbols=int(input("How many symbols do you want in your password?"))
n_numbers=int(input("How many numbers do you want in your password?"))
password_list=[]

for i in range(1,n_letters+1):
  char=random.choice(letters)
  password_list.append(char)
print(password_list)

for i in range(1,n_numbers+1):
  char=random.choice(numbers)
  password_list.append(char)
print(password_list)

for i in range(1,n_symbols+1):
  char=random.choice(symbols)
  password_list.append(char)

print("password before shuffling is",password_list)

for i in password_list:
  random.shuffle(password_list)

print("Password after shuffling is",password_list)

password=""

for i in password_list:
  password+=i
print("password generated is",password)