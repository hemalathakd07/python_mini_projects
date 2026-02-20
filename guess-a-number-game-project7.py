#project 7:
#guess the correct number:

import random
import logo_art

def set_difficulty(level_of_difficulty):
    if level_of_difficulty=="easy":
        no_of_attempts=10
        return no_of_attempts
    elif level_of_difficulty=="hard":
        no_of_attempts=5
        return no_of_attempts
    
def check_answer(guessed_number,generated_number,attempts):
    if guessed_number<generated_number:
        print("Your guess is too low")
        attempts=attempts-1
        return attempts
    elif guessed_number>generated_number:
        print("Your guess is too high")
        attempts=attempts-1
        return attempts
    elif guessed_number==generated_number:
        print(f"Your guess is correct ... The answer was {generated_number}")



generated_number=random.randint(1,50)

def game():
    print(logo_art.logo)
    print("Let me think of a number between 1 to 50")
    level_of_difficulty=input("Choose the level of difficulty...Tyope 'easy' or 'hard':").lower()

    guessed_number=0
    attempts=set_difficulty(level_of_difficulty)
    while guessed_number!=generated_number:
        print(f"You have {attempts} remaining sttempts to guess the number")
        guessed_number=int(input("Guess a number:"))
        attempts=check_answer(guessed_number,generated_number,attempts)
        if attempts==0:
            print("You are out of guessess...You lose!")
            return
            
        elif guessed_number!=generated_number:
            print("Guess again")

game()