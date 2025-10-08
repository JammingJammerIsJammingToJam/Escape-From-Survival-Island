import random
import time
import os

#Checks validity of input as an integer from 0 to max
def valid_input(question, max):
  while True:
    answer = input(question)
    try:
      answer = int(answer)
    except:
      print("Please enter a valid input")
      continue
    if answer < 0 or answer > max:
      print("Please enter a valid input")
      continue
    break
  return answer

#Selects a seed
def seed_select():
  set_seed = valid_input("Do you want a set seed (1) or not (0)? ", 1)
  if set_seed == 1:
    seed = valid_input("Enter a seed ", 4_294_967_295)
    random.seed(seed)
      
#Character Creation

#Shop

#Island

#Journey

#Final Score

#Gameplay loop
def main():
  os.system("clear")
  speed = valid_input("Speed in seconds (max is 10) ", 10)
  os.system("clear")
  print("Escape from Survival Island")
  
  
