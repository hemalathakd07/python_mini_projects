print("---Welcome to pizza order program---")
pizza_size=input("Select the size of the pizza (s for small,m for medium,l for large)")
bill=0
if pizza_size=='s' or pizza_size=='S':
  bill+=140
  print(f"Bill price of the small size pizza is {bill} rupees")
elif pizza_size=='m' or pizza_size=='M':
  bill+=180
  print(f"Bill price of the medium size pizza is {bill} rupees")
elif pizza_size=='l' or pizza_size=='L':
  bill+=230
  print(f"Bill price of the large size pizza is {bill} rupees")
else:
  print("Invalid input")
  exit()

add_pepperoni=input("Do you want to add pepperoni (enter y for yes)")
if add_pepperoni=='y' or add_pepperoni=='Y':
  if pizza_size=='s' or pizza_size=='S':
    bill+=30
    print("30 rupees is added to your bill")
  else:
    bill+=50
    print("50 rupees is added to your bill")
else:
  print("invalid input entered")

extra_cheese=input("Do you want to add extra cheese(enter y for yes)")
if extra_cheese=='y' or extra_cheese=='Y':
  bill+=20
  print("20 rupees is added to your bill")
else:
  print("entered input is invalid")

print(f"The total price of your pizza is {bill} rupees")