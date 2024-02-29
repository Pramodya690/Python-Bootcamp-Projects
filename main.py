#Number Guessing Game Objectives:

# from art import logo
# print(logo)

import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, random_number):
  if guess > random_number:
    print("You are too high")
  elif guess < random_number:
    print("You are too low")
  elif guess == random_number:
    print("YOU WIN")
  
def set_difficulty():
  difficulty_level = input("Enter Difficulty level - easy/hard:  ")
  if difficulty_level == "easy":
    return EASY_LEVEL_TURNS
    print("You have 10 total attempts")
  else:
    return HARD_LEVEL_TURNS

def game():
  random_number = random.randint(1, 100)
  #print(random_number)
  
  attempts = set_difficulty()
  print(f"You have {attempts} attempts remaining")
  guess = 0
  
  while guess != random_number:
    
    guess = int(input("Make a guess:  "))
    
    check_answer(guess, random_number)

game()








 
  
  
