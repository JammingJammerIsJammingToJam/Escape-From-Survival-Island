"""
TODO:
Journey: - Done
  Building - Done
  Repair - Done
  Random Events - Done
  Calculations Phase - Done
Final Score:
  Scoring Calculation - Planning
  Ranks - Planning
Story: 
  Add story - Planning
Plan:
  Finish Game Plan - In Progress
  Do Coding Plan - Not Started
Sleep:
  Add time.sleep(speed) anywhere necessary - In Progress
Comments:
  Add comments
Bug Fixing:
  Find bugs
  Fix bugs
Variables:
  Fix Variable Names
"""


#Libraries
import random
import time
import os
import math

#Initialising variables to be used between procedures
speed = 0
name = ""
max_health = 10
action_modifier = 0
cash = 100

difficulty = 0 #0 is easy while 5 is extreme
points = 0

itemnames = ["wood", "rope", "nails", "fabric", "bandages", "food", "glowing rock"]
items = [0, 0, 0, 0, 0, 0, 1]

names = ["Dineth's", "Jay's", "Chris's", "Danny's"]

#Checks validity of input as an integer from 0 to max
def valid_input(question, max):
  while True:
    answer = input(question)
    try: #Checks if it is an integer
      answer = int(answer)
    except:
      print("Please enter a valid input")
      continue
    if answer < 0 or answer > max or answer - round(answer) != 0: #Checks whether the integer is correct
      print("Please enter a valid input")
      continue
    break
  return answer

#Selects a seed
def seed_select():
  global speed
  set_seed = valid_input("Do you want a set seed (1) or not (0)? ", 1)
  if set_seed == 1: #The user picks a seed
    seed = valid_input("Enter a seed ", 4_294_967_295)
    random.seed(seed)
  else: #The seed is random
    seed = random.randint(0, 4_294_967_295)
    random.seed(seed)
    print("Your Seed is", seed)
    time.sleep(speed)

#Select difficulty from 0 to 5
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

  #Asks for the name of the character
  name = str(input("What is your name? "))
  time.sleep(speed)
  
  #Transforms difficulty into spendable points with the formula 30-5d
  points = 30 - difficulty * 5
  print("You have", points, "points to spend")

  #HP = 1P + 10
  max_health += valid_input("How many points in health? ", points)
  points -= max_health - 10
  time.sleep(speed)

  """ Invest points into the Action Modifier that is added or subtracted from rolls for an advantage
  Created by the formula AM = 3P """
  maximum = 3
  if points < 9:
    maximum = math.floor(points/3)
  action_modifier = valid_input("How many points for the action modifier? (1 AM for 3 points) (max input is 3AM) ", maximum)
  points -= action_modifier * 3
  time.sleep(speed)
  del maximum

  #C = 100P + 100
  cash *= valid_input("How many points in cash? (100 for 1 point) ", points) + 1
  points -= cash / 100 - 1

shop_prices = []
original_items = 20
#Shop
def shop():
  global original_items
  global shop_prices
  global speed
  global items
  global itemnames
  global cash
  global name
  global names
  global action_modifier

  print("Welcome to", random.choice(names), "shop!")
  time.sleep(speed)

  #Randomises the inventory and prices of the shop with the AM included to give advantage on rolls
  shop_items = [random.randint(original_items, 50 + action_modifier) for i in range(0, 6)]
  shop_prices = [random.randint(1, 10 - action_modifier) for i in range(0, 6)]
  time.sleep(speed)

  while True:
    
    print("You have", cash, "cash")
    time.sleep(speed)

    print("This shop sells: ")
    time.sleep(speed)

    #Outputs the inventory of the shop and its prices
    for i in range(0, 6):
      print(" ", shop_items[i], itemnames[i], "for", shop_prices[i], "cash each")
      time.sleep(speed)
    
    #Asks the user for an input
    kale = valid_input("What do you want (0) - wood... (6) - display inventory (7) - exit ", 7)
    time.sleep(speed)

    #Displays the user's inventory
    if kale == 6:
      print("You have", end=" ")
      for i in range(0, 5):
        print(items[i], itemnames[i], end=", ")
      print(items[5], itemnames[5], end=".\n")
      time.sleep(speed)
      continue

    #Exits the shop
    elif kale == 7:
      break

    #How much and whether the user is buying or selling
    jam = valid_input("Buy (0) or Sell (1)? ", 1)
    apple = valid_input("How much? ", shop_items[kale])
    time.sleep(speed)

    #Calculates the total cost
    cost = apple * shop_prices[kale]

    #Buying
    if jam == 0:
      if cost > cash: #Not enough cash
        print("You don't have enough money")
        continue
      else: #Enough cash
        cash -= cost
        items[kale] += apple
        shop_items[kale] -= apple
    
    #Selling
    else:
      if items[kale] < apple: #Not enough items
        print("You don't have enough items")
        continue
      else: #Enough items
        cash += math.floor(0.8 * cost) #Buyback is 80% of buy price
        items[kale] -= apple
        shop_items[kale] += apple

shipname = ""
shiphealth = 0
shipspeed = 0
#Shipyard
def shipyard():
  global original_items
  global shipname
  global shiphealth
  global shipspeed
  global speed
  global shop_prices
  global items
  global itemnames
  global cash
  global name
  global action_modifier
  original_items = 1

  os.system("clear")
  time.sleep(speed)

  #Declare ship variables
  available_ships = ["Raft", "Sailboat", "Yacht", "Galleon"]
  #wood - rope - nails - fabric (item order)
  """
  Randomises the item cost for ship repair
  The raft is always free
  From that point on
  The cost for each item for each ship is between
  10 - AM
  and
  (index+1)*10 - AM
  """
  ship_repair = [[0, 0, 0, 0], [random.randint(10 - action_modifier, 20 - action_modifier) for i in range(0, 4)], [random.randint(10 - action_modifier, 30 - action_modifier) for i in range(0, 4)], [random.randint(10 - action_modifier, 30 - action_modifier) for i in range(0, 4)]]
  ship_prices = [0]
  #Calculates the cost of the ship with the previously randomised item prices and ship item costs with a markup of ~20%
  ship_prices += [round(sum(shop_prices[i] * ship_repair[j][i] * 1.2 for i in range(0, 4))) for j in range(1, 4)]
  print("You enter the Shipyard...")
  time.sleep(speed)
  print("You approach the Harbourmaster...")
  time.sleep(speed)
  print("He points at 4 ships: ")
  #Outputs ships and their item and cash cost
  for i in range(0, 4):
    print("The", available_ships[i], "needs", end = " ")
    for j in range(0, 2):
      print(ship_repair[i][j], itemnames[j], end = ", ")
    print(ship_repair[i][2], itemnames[2], end = " and ")
    print(ship_repair[i][3], itemnames[3], "or", ship_prices[i], end = " cash.\n")
    time.sleep(speed)
  text = "Raft (0), Sailboat (1), Yacht (2), or Galleon (3) "
  maximum = 3
  if items[6] == 1: #Secret item obtained after a certain score is reached
    print("Noticing your glowing rock, the Harbourmaster points out a shipwrecked submarine at the end of the bay")
    time.sleep(speed)
    text = "Raft (0), Sailboat (1), Yacht (2), Galleon (3) or Submarine (4) "
    maximum += 1
    available_ships.append("Submarine")
  while True: #Purchasing loop
    kale = valid_input("Buy (0) or Fix (1)? ", 1)
    time.sleep(speed)
    apple = valid_input(text, maximum)
    time.sleep(speed)
    if apple == 4 and kale == 0: #Player cannot buy the sub, only repair with the glowing rock
      print("You can't buy that")
      continue
    elif apple == 4:
      break
    #Checks whether you have enough to get the ship
    not_enough = 0
    for i in range(0, 4):
      if items[i] < ship_repair[apple][i] and kale == 1:
        print("You don't have enough items")
        not_enough = 1
        break
      elif ship_prices[apple] > cash and kale == 0:
        print("You don't have enough cash")
        not_enough = 1
        break
    if not_enough == 1:
      continue
    break
  if kale == 0: #Buying
    cash -= ship_prices[apple]
    print("You bought the", available_ships[apple])
  elif apple != 4: #Fixing the ordinary ships
    for i in range(0, 4):
      items[i] -= ship_repair[apple][i]
    print("You fixed the", available_ships[apple])
  else: #The glowing rock is not used up
    print("You fixed the submarine")
  time.sleep(speed)
  """
  Name - Speed - Health:
  Raft - 1 - 5
  Sailboat - 2 - 10
  Yacht - 3 - 15
  Galleon - 4 - 20
  Submarine - 5 - 25
  """
  shipname = available_ships[apple]
  shipspeed = apple + 1
  shiphealth = (apple + 1) * 5
  #print(shipname, shipspeed, shiphealth, cash)
  #time.sleep(speed)


days = 0
distance = 0
#Journey
def journey():
  global days
  global shipname
  global shipspeed
  global itemnames
  global items
  global shiphealth
  maxship = shiphealth
  global cash
  global action_modifier
  global name
  global max_health
  global distance
  health = max_health
  hunger = 100
  #Net (Pick up raw materials and occasionally fish) - Farm (Food) - Loom (Bandages)
  buildings = [0, 0, 0]
  buildingnames = ["Net", "Farm", "Loom"]
  """
  Wood - Rope - Nails - Fabric
  Randomises the build cost between
  4 - AM
  and
  8 - AM
  For each material
  For each item
  """
  buildingscost = [[random.randint(4 - action_modifier, 8 - action_modifier) for i in range(0, 4)] for j in range(0, 3)]
  #Action Phase
  current_repair = random.randint(0, 4) #What the ship currently needs for repair
  repair_amount = random.randint(1, 6 - action_modifier)
  #Initialises 20 events
  #You have a chance at reaching land after day 5
  events = ["You Arrive at Land - Your Journey is Over!",
            "You encounter a Floating Trading Post",
            "You encounter a Floating Trading Post",
            "You encounter a Floating Trading Post",
            "You encounter a Floating Trading Post",
            "You Pray To Eleuxaos and you are granted a boon!",
            "You get a wonderful night's sleep", 
            "A fish washes up on your boat", 
            "You ride the currents - travelling twice as far today!", 
            "You find some flotsam floating", 
            "The Angels of Eleuxaos get to work!",
            "The winds were unfavourable - you traveled half as far...", 
            "You got scurvy from a lack of Vitamin C", 
            "You are attacked by a Pirate Crew", 
            "You get a fever!", 
            "You pray to Eleuxaos but nothing appears...",
            "Some of your supplies are washed away by a wave...", 
            "A Storm batters you and your ship", 
            "A Kraken attacks your ship!", 
            "Rhamnaer strikes you with his Karambit!"]
  while True:
    days += 1
    time.sleep(speed)
    print("It is Day", days, "of the voyage")
    time.sleep(speed)
    while True:
      #Status report
      print("")
      print("Your health is at", str(health) + "/" + str(max_health))
      print("Your hunger is at", str(hunger) + "/100")
      print("Your shiphealth is at", str(shiphealth) + "/" + str(maxship))
      #Possible Actions
      action = valid_input("Repair the " + shipname + " (0), Build (1), Eat Food (2), Use Bandages (3), View Inventory (4), or Set Sail (5)? ", 5)
      if action == 5: #Set Sail
        print("The", shipname, "sets sail!")
        break
      elif action == 4: #View inventory
        print("You have", end=" ")
        #Cycles through the item lists and prints out how many you have
        for i in range(0, 5):
          print(items[i], itemnames[i], end=", ")
        print(items[5], itemnames[5], end=" and ")
        print(cash, "cash", end=".\n")
        time.sleep(speed)
        continue
      elif action == 3: #Use Bandages
        if items[4] == 0:
          print("You don't have any bandages!")
          time.sleep(speed)
          continue
        #Calculates the maximum number of bandages
        deficit = max_health - health
        if deficit == 0: #No bandages needed
          print("You are at max health")
          time.sleep(speed)
          continue
        maxbandage = math.ceil(deficit / 3) #3HP = 1 Bandage
        if items[4] < maxbandage: #You don't have enough for full health
          maximum = items[4]
        else: #You have enough bandages for full health
          maximum = maxbandage
        del maxbandage #Save a little RAM
        bandages = valid_input("How many bandages? ", maximum)
        items[4] -= bandages
        bandages *= 3
        #Calculates new health
        if bandages <= deficit:
          health += bandages
          print(f"You healed {bandages} HP!")
        else:
          health += deficit
          print(f"You healed {deficit} HP!")
        time.sleep(speed)
      elif action == 2: #Eating food
        #Checks for hunger and inventory
        if items[5] == 0:
          print("You don't have any food!")
          time.sleep(speed)
          continue
        deficit = 100 - hunger #Hunger is calculated as Hunger/100
        if deficit == 0:
          print("You aren't hungry")
          time.sleep(speed)
          continue
        maxfood = math.ceil(deficit / 5) #5HP = 1 Food
        if items[5] < maxfood: #Not enough food for full hunger
          maximum = items[5]
        else: #Enough food for full hunger
          maximum = maxfood
        del maxfood #Save a little RAM
        food = valid_input("How much food? ", maximum)
        items[5] -= food
        food *= 5
        #Calculates new hunger
        if food <= deficit:
          hunger += food
          print(f"You gained {food} hunger!")
        else:
          hunger += deficit
          print(f"You gained {deficit} hunger!")
        time.sleep(speed)
      elif action == 1: #Building
        #Outputs the buildings' cost
        for i in range(0, 3):
          print("The", buildingnames[i], "needs", end = " ")
          for j in range(0, 2):
            print(buildingscost[i][j], itemnames[j], end = ", ")
            time.sleep(speed)
          print(buildingscost[i][2], itemnames[2], end = " and ")
          time.sleep(speed)
          print(buildingscost[i][3], itemnames[3], end = ".\n")
          time.sleep(speed)

        thing_to_build = valid_input("What do you want to build: Net (0), Farm (1), Loom (2) or Exit (3)? ", 3)
        time.sleep(speed)

        if thing_to_build == 3: #Exit
          continue

        #Checks inventory levels
        not_enough = 0
        for i in range(0, 4):
          if items[i] < buildingscost[thing_to_build][i]:
            print("You don't have enough items")
            not_enough = 1
            break
        if not_enough == 1: #Not enough items
          time.sleep(speed)
          continue

        for i in range(0, 4): #Removes items from inventory
          items[i] -= buildingscost[thing_to_build][i]
        
        print("You built a", buildingnames[thing_to_build], end = "!\n")
        time.sleep(speed)

        buildings[thing_to_build] += 1 #Builds the building

        buildingscost[thing_to_build] = [random.randint(4 - action_modifier, 8 - action_modifier) for i in range(0, 4)] #Randomises the building's cost

      elif action == 0: # Repairing the ship
        if shiphealth == maxship:
          print("Your ship is at full HP")
          continue
        deficit = maxship - shiphealth
        #Status Report
        print("Your shiphealth is at", str(shiphealth) + "/" + str(maxship))
        time.sleep(speed)
        print("It will take", repair_amount, itemnames[current_repair], "to fix by 5HP")
        time.sleep(speed)
        option = valid_input("Repair (0) or Exit (1)? ", 1)
        time.sleep(speed)
        if option == 1: #Exit
          continue
        if items[current_repair] < repair_amount: #Not enough items
          print("You don't have enough items")
          continue
        items[current_repair] -= repair_amount
        #Calculates new shiphealth
        if deficit < 5:
          shiphealth = maxship
        else:
          shiphealth += 5
    #Event Phase
    distance_multiplier = 1
    if days < 5: #You can only finish the journey after Day 5
      event = random.randint(1, len(events) - action_modifier - 1)
    else:
      event = random.randint(0, len(events) - action_modifier - 1)
    print(events[event])
    time.sleep(speed)
    if event == 0: #Arrival - ends game
      return 0
    elif event in [1, 2, 3, 4]: #Trading Post - shop 
      shop()
    elif event == 5: #Successful Prayer - gives items
      for i in range(0, 6):
        change = random.randint(1, 3+action_modifier)
        items[i] += change
        print("You received", change, itemnames[i], "!")
        time.sleep(speed)
    elif event == 6: #Good night's sleep - heals
      deficit = max_health - health
      change = random.randint(1, 3+action_modifier)
      if deficit == 0: #Full health
        print("You already have full health")
      #Calculates health
      elif deficit < change:
        health = max_health
        print("You gained", deficit, "health!")
      else:
        health += change
        print("You gained", change, "health!")
      time.sleep(speed)
    elif event == 7: #Fish on your boat - gives food
      change = random.randint(1, 3+action_modifier)
      items[5] += change
      print("You gained", change, "food!")
      time.sleep(speed)
    elif event == 8: #Currents - 2x dist
      distance_multiplier = 2
    elif event == 9: #Flotsam - gives items
      picked_item = random.randint(0, 4)
      change = random.randint(1, 3+action_modifier)
      print(f"You picked up {change} {itemnames[picked_item]}!")
      items[picked_item] += change
      time.sleep(speed)
      del picked_item
    elif event == 10: #Random building
      thing_to_build = random.randint(0, 3)
      print(f"The Angels bless you with a new {buildingnames[thing_to_build]}!")
      buildings[thing_to_build] += 1
    elif event == 11: #Bad winds - 0.5x dist
      distance_multiplier = 0.5
    elif event == 12: #Scurvy - Deals damage
      change = random.randint(1, 5-action_modifier)
      health -= change
      print(f"You took {change} damage!")
      time.sleep(speed)
    elif event == 13: #Pirates - lose items
      for i in range(0, 4):
        if items[i] < 3: #Can lose max 3 of each item
          maximum = items[i]
        else:
          maximum = 3
        change = random.randint(0, maximum)
        if change == 0:
          print(f"You lost no {itemnames[i]}!")
        else:
          print(f"You lost {change} {itemnames[i]}!")
        time.sleep(speed)
        items[i] -= change
    elif event == 14: #Fever - Deals damage
      change = random.randint(1, 5-action_modifier)
      health -= change
      print(f"You took {change} damage!")
      time.sleep(speed)
    
    #15 - nothing happens

    elif event == 16: #Supplies washed away - lose items
      for i in range(0, 6):
        if items[i] == 0: #No items
          print("You didn't have any", itemnames[i], "in the first place!")
          time.sleep(speed)
          continue
        change = random.randint(1, 5-action_modifier)
        if items[i] <= change: #Lost everything
          items[i] = 0
          print("You lost all of your", itemnames[i], end = "!\n")
        else: #Didn't lose everything
          items[i] -= change
          print("You lost", change, itemnames[i], end = "!\n")
        time.sleep(speed)
    
    elif event == 17: #Storm - deals damage to player and ship
      #Player Damage
      change = random.randint(1, 5-action_modifier)
      health -= change
      print(f"You took {change} damage!")
      time.sleep(speed)
      #Ship Damage
      change = random.randint(1, 7-action_modifier)
      shiphealth -= change
      print(f"Your ship took {change} damage!")
      time.sleep(speed)
    elif event == 18: #Kraken - deals damage to player and ship
      #Player Damage
      change = random.randint(1, 6-action_modifier)
      health -= change
      print(f"You took {change} damage!")
      time.sleep(speed)
      #Ship Damage
      change = random.randint(1, 8-action_modifier)
      shiphealth -= change
      print(f"Your ship took {change} damage!")
      time.sleep(speed)
    elif event == 19: #Rhamnaer and his karambit - deals damage to player and ship
      #Player Damage
      change = random.randint(1, 7-action_modifier)
      health -= change
      print(f"You took {change} damage!")
      time.sleep(speed)
      #Ship Damage
      change = random.randint(1, 9-action_modifier)
      shiphealth -= change
      print(f"Your ship took {change} damage!")
      time.sleep(speed)

    #Starvation Check
    if hunger == 0:
      change = random.randint(0, 4-action_modifier)
      health -= change
      print(f"You lost {change} health due to starvation!")

    #Player Death Check
    if health <= 0:
      print("You died!")
      time.sleep(speed)
      return 1
    
    #Ship Broken Check
    if shiphealth <= 0:
      print(f"Your {shipname} broke!")
      return 1
  
    #Calculations Phase
    hunger -= random.randint(5, 10-action_modifier)  #Calculates new hunger value
    if hunger < 0:
      hunger = 0
    
    #Calculates items gained from nets
    changes = [0, 0, 0, 0, 0]
    for i in range(buildings[0]): #Which nets got which stuff
      changes[random.randint(0, 5)] += 1
    for i in range(4): #How much of said stuff did the nets gather
      change = sum(random.randint(0, 1+action_modifier) for j in range(changes[i]))
      print(f"Your nets gathered {change} {itemnames[i]}!")
      items[i] += change
      time.sleep(speed)
    change = sum(random.randint(0, 1+action_modifier) for j in range(changes[4])) #Food/Fish because it is a different place in the items list
    print(f"Your nets gathered {change} fish!")
    items[5] += change
    time.sleep(speed)

    #Calculates items gained from farms
    change = sum(random.randint(0, 2+action_modifier) for i in range(buildings[1]))
    print(f"You gained {change} food from your farms!")
    items[5] += change
    time.sleep(speed)

    #Calculates loom bandage production
    change = sum(random.randint(0, 1) for i in range(buildings[2]))
    print(f"You gained {change} bandages from your looms")
    items[4] += change
    time.sleep(speed)

    #Calculates distance travelled
    change = random.randint(1, 3+action_modifier) * shipspeed * distance_multiplier
    distance += change
    print(f"You sailed {change} miles!")
    time.sleep(speed)

    #Separates each day
    print("")
    print("****************************")
    print("")

#Final Score
#def final_score(outcome):
  #score = 0

  #return score

#Setup
def setup():
  global speed

  os.system("clear")
  while True: #Calculates game speed 1-10s
    speed = valid_input("Speed in seconds (max is 10) ", 10)
    if speed != 0:
      break
    else:
      print("Enter a value greater than 0")

  os.system("clear")
  print("Escape from Survival Island")
  time.sleep(speed)

  #Checks for game start
  start = valid_input("Start game (1) or quit (0) ", 1)
  if start == 0:
    quit()
  del start

  #Selects a seed
  os.system("clear")
  seed_select()
  time.sleep(speed)

  #Selects the difficulty
  os.system("clear")
  difficulty_selection()
  time.sleep(speed)

  #Goes into the character creation menu
  character_creation()
  time.sleep(speed)
  os.system("clear")

#Gameplay loop
def main():
  setup()
  shop()
  shipyard()
  journey()
  #final_score()
  
main()
