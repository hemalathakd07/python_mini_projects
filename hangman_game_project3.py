import random

import hangman_stages

word_list=["papaya","banana","apple","guava","pomogranate"]

choosen_word=random.choice(word_list)
display=[]

for i in range(len(choosen_word)):
  display+='_'

lives=6
print(f"You have only {lives} lives to guess the choosen word! Good luck!!")
print(display)

game_over=False

while not game_over:
  guessed_letter=input("Guess a letter:").lower()
  for position in range(len(choosen_word)):
    letter=choosen_word[position]
    if letter==guessed_letter:
      display[position]=guessed_letter
  print(display)
  
  if guessed_letter not in choosen_word:
    lives-=1
    if lives==0:
      game_over=True
      print("you lose!")
  
  if '_' not in display:
    game_over=True
    print("you won!!")

  print(hangman_stages.HANGMANPICS[lives])