import random
import time
import os
import math

speed = 0
name = ""
max_health = 10
action_modifier = 0
cash = 100

difficulty = 0
points = 0

itemnames = ["wood", "rope", "nails", "fabric", "bandages", "food", "glowing rock"]
items = [0, 0, 0, 0, 0, 0, 0]

names = ["Dineth's", "Jay's", "Chris's", "Danny's"]

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
  global speed
  set_seed = valid_input("Do you want a set seed (1) or not (0)? ", 1)
  if set_seed == 1:
    seed = valid_input("Enter a seed ", 4_294_967_295)
    random.seed(seed)
  else:
    seed = random.randint(0, 4_294_967_295)
    random.seed(seed)
    print("Your Seed is", seed)
    time.sleep(speed)

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

  maximum = 3
  if points < 9:
    maximum = math.floor(points/3)
  action_modifier = valid_input("How many points for the action modifier? (1 AM for 3 points) (max input is 3AM) ", maximum)
  points -= action_modifier * 3
  time.sleep(speed)
  del maximum

  cash *= valid_input("How many points in cash? (100 for 1 point) ", points) + 1
  points -= cash / 100 - 1

shop_prices = []
#Shop
def shop():
  global shop_prices
  global speed
  global items
  global itemnames
  global cash
  global name
  global names
  print("Welcome to", random.choice(names), "shop!")
  time.sleep(speed)
  shop_items = [random.randint(1, 50) for i in range(0, 6)]
  shop_prices = [random.randint(1, 10) for i in range(0, 6)]
  time.sleep(speed)
  while True:
    print("You have", cash, "cash")
    time.sleep(speed)
    print("This shop sells: ")
    time.sleep(speed)
    for i in range(0, 6):
      print(" ", shop_items[i], itemnames[i], "for", shop_prices[i], "cash each")
      time.sleep(speed)
    kale = valid_input("What do you want (0) - wood... (6) - display inventory (7) - exit ", 7)
    if kale == 6:
      print("You have", end=" ")
      for i in range(0, 5):
        print(items[i], itemnames[i], end=", ")
      print(items[5], itemnames[5], end=".\n")
      continue
    elif kale == 7:
      break
    time.sleep(speed)
    apple = valid_input("How much do you want? ", shop_items[kale])
    time.sleep(speed)
    cost = apple * shop_prices[kale]
    if cost > cash:
      print("You don't have enough money")
      continue
    else:
      cash -= cost
      items[kale] += apple
      shop_items[kale] -= apple

#Shipyard
def shipyard():
  global speed
  global shop_prices
  global items
  global itemnames
  global cash
  global name
  global action_modifier
  os.system("clear")
  time.sleep(speed)
  available_ships = ["Raft", "Sailboat", "Yacht", "Galleon"]
  #wood - rope - nails - fabric
  ship_repair = [[0, 0, 0, 0], [random.randint(10 - action_modifier, 20 - action_modifier) for i in range(0, 4)], [random.randint(10 - action_modifier, 30 - action_modifier) for i in range(0, 4)], [random.randint(10 - action_modifier, 30 - action_modifier) for i in range(0, 4)]]
  ship_prices = [0]
  ship_prices += [sum(shop_prices[i] * ship_repair[j][i] for i in range(0, 4)) for j in range(1, 4)]
  print("You enter the Shipyard...")
  time.sleep(speed)
  print("You approach the Harbourmaster...")
  time.sleep(speed)
  print("He points at 4 ships: ")
  for i in range(0, 4):
    print("The", available_ships[i], "needs", end = " ")
    for j in range(0, 3):
      print(ship_repair[i][j], itemnames[j], end = ", ")
    print(ship_repair[i][3], itemnames[j], end = ".\n")


#Journey
#def journey():
  #Action Phase

  #Event Phase

  #Death Check

  #Secondary Action Phase

  #Calculations Phase

#Final Score
#def final_score():
  #score = 0

  #return score

#Setup
def setup():
  global speed
  os.system("clear")
  while True:
    speed = valid_input("Speed in seconds (max is 10) ", 10)
    if speed != 0:
      break
    else:
      print("Enter a value greater than 0")

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
  #journey()
  #final_score()
  

main()
