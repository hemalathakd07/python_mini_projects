import project9_logo
import random
import game_database
import os

print(project9_logo.logo)


def display_accountinfo(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return (f"{name},a {description} from {country}")

def check_answer(guess,followers1,followers2):
    if followers1<followers2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False

account2=random.choice(game_database.data)

continue_flag=True
score=0
while continue_flag:
    account1=account2
    account2=random.choice(game_database.data)

    while account1==account2:
        account2=random.choice(game_database.data)


    print(f"compare 1:{display_accountinfo(account1)}")
    print(project9_logo.vs)
    print(f"compare 2:{display_accountinfo(account2)}")


    guess=int(input("Who has more followers? Type 1 or 2:"))

    followers1=account1["follower_count"]
    followers2=account2["follower_count"]

    print(followers1)
    print(followers2)

    is_correct=check_answer(guess,followers1,followers2)
    print(os.system("cls"))
    print(project9_logo.logo)

    if is_correct==True:
        score=score+1
        print(f"You are right. Your score is {score}")
        
    else:
        print(f"You are wrong.Your final score is {score}")
        continue_flag=False