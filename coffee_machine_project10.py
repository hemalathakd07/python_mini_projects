menu={
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24
        },
        "cost":150
    },
    "espresso":{
        "ingredients":{
            "water":50,
            "milk":120,
            "coffee":18
        },
        "cost":100
    },
    "cappuccino":{
        "ingredients":
        {
            "water":250,
            "milk":100,
            "coffee":24
        },
        "cost":200
    }
}

profit=0
resources={
    "water":500,
    "milk":200,
    "coffee":100
}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is no enough {item}")
            return False
    return True

def process_coins():
    print("please insert coins:")
    total=0
    coins_five_rupees=int(input("How many 5Rs coind?"))
    coins_ten_rupees=int(input("How many 10Rs coins?"))
    coins_twenty_rupees=int(input("How many 20Rs coins?"))
    total=coins_five_rupees*5+coins_ten_rupees*10+coins_twenty_rupees*20
    return total

def is_payment_successful(money_received,cost_of_coffee):
    if money_received>=cost_of_coffee:
      global profit
      profit+=cost_of_coffee  
      change=money_received-cost_of_coffee
      print(f"Here is your change Rs{change}")
      return True
    else:
        print("Sorry that's not enough money.Money refunded")
        return False
    
def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item]-=coffee_ingredients[item]
    print(f"here is your {coffee_name}☕.. Enjoy")

is_on=True
while is_on:
    choice=input("What would you like to have ?(latte/espresso/cappuccino)...enter 'off' to switch off the machine and enter 'report' to get the report :")
    if choice=='off':
        is_on=False
    elif choice=="report":
        print(f"Water={resources['water']}ml")
        print(f"Milk={resources['milk']}ml")
        print(f"Coffee={resources['coffee']}g")
        print(f"Money=Rs{profit}")
    else:
        coffee_type=menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment=process_coins()
            if(is_payment_successful(payment,coffee_type['cost'])):
                make_coffee(choice,coffee_type['ingredients'])