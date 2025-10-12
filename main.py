import random
import time
import os

speed = 0
name = ""
max_health = 10
action_modifier = 0
cash = 100

difficulty = 0
points = 0

#Wood, Rope, Nails, Fabric, Bandages, Food, Glowing Rock
items = [0, 0, 0, 0, 0, 0, 0]

#Checks validity of input as an integer from 0 to max
def valid_input(question, max):
  while True:
    answer = input(question)
    try:
      answer = int(answer)
    except:
      print("Please enter a valid input")
      continue
    if answer < 0 or answer > max or answer - round(answer) != 0:
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
  else:
    seed = random.randint(0, 4_294_967_295)
    random.seed(seed)
    print("Your Seed is", seed)

#Difficulty selection
def difficulty_selection():
  global difficulty
  difficulty = valid_input("Select a difficulty (0) - easy, (5) - extreme ", 5)

#Character Creation
def character_creation():
  global speed
  global difficulty
  global name
  global max_health
  global action_modifier
  global cash
  global points

  name = str(input("What is your name? "))
  time.sleep(speed)
  points = 30 - difficulty * 5

  print("You have", points, "points to spend")

  max_health += valid_input("How many points in health? ", points)
  points -= max_health - 10
  time.sleep(speed)

  if points < 3:
    maximum = points
  else:
    maximum = 3
  action_modifier = valid_input("How many points for the action modifier? (max is 3) ", maximum)
  points -= action_modifier
  time.sleep(speed)
  del maximum

  cash *= valid_input("How many points in cash? (100 for 1 point) ", points) + 1
  points -= cash / 100 - 1
  
#Shop
def shop():


#Shipyard
def shipyard():


#Journey
def journey():


#Final Score
def final_score():
  score = 0

  return score

#Setup
def setup():
  os.system("clear")
  speed = valid_input("Speed in seconds (max is 10) ", 10)

  os.system("clear")
  print("Escape from Survival Island")
  time.sleep(speed)

  start = valid_input("Start game (1) or quit (0) ", 1)
  if start == 0:
    quit()
  del start

  os.system("clear")
  seed_select()
  time.sleep(speed)

  os.system("clear")
  difficulty_selection()
  time.sleep(speed)

  character_creation()
  time.sleep(speed)
  os.system("clear")

#Gameplay loop
def main():
  setup()
  shop()
  shipyard()
  journey()
  final_score()
  
while True:
  main()
