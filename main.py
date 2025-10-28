"""
TODO:
Journey: - Done
  Building - Done
  Repair - Done
  Random Events - Done
  Calculations Phase - Done
Final Score:
  Scoring Calculation - Done
  Ranks - Done
Story: 
  Add story - Done
Plan:
  Game Plan - Done
  Coding Plan - Done
Sleep:
  Add time.sleep(speed) anywhere necessary - Done
Comments:
  Add comments - Done
Bug Fixing: - THIS
  Find bugs
  Fix bugs
Variables:
  Fix Variable Names - Done
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
  Created by the formula AM = 5P """
  maximum = 5
  if points < 15:
    maximum = math.floor(points/5)
  print("The action modifier changes the results of random rolls")
  print("For 1 AM, you need 5 points")
  print("You need to input the number of AM you want")
  print("For instance, if you enter 2, you spend 10 points")
  action_modifier = valid_input("How many points for the action modifier? ", maximum)
  points -= action_modifier * 5
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
    option = valid_input("What do you want (0) - wood ... (6) - display inventory (7) - exit ", 7)
    time.sleep(speed)

    #Displays the user's inventory
    if option == 6:
      print("You have", end=" ")
      for i in range(0, 5):
        print(items[i], itemnames[i], end=", ")
      print(items[5], itemnames[5], end=".\n")
      time.sleep(speed)
      continue

    #Exits the shop
    elif option == 7:
      break

    #How much and whether the user is buying or selling
    buy_sell = valid_input("Buy (0) or Sell (1)? ", 1)
    if buy_sell == 0:
      how_much = valid_input("How much? ", shop_items[option])
    else:
      how_much = valid_input("How much? ", items[option])
    time.sleep(speed)

    #Calculates the total cost
    cost = how_much * shop_prices[option]

    #Buying
    if buy_sell == 0:
      if cost > cash: #Not enough cash
        print("You don't have enough money")
        continue
      else: #Enough cash
        cash -= cost
        items[option] += how_much
        shop_items[option] -= how_much
    
    #Selling
    else:
      if items[option] < how_much: #Not enough items
        print("You don't have enough items")
        continue
      else: #Enough items
        cash += math.floor(0.8 * cost) #Buyback is 80% of buy price
        items[option] -= how_much
        shop_items[option] += how_much

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
    buy_sell = valid_input("Buy (0) or Fix (1)? ", 1)
    time.sleep(speed)
    ship_number = valid_input(text, maximum)
    time.sleep(speed)
    if ship_number == 4 and buy_sell == 0: #Player cannot buy the sub, only repair with the glowing rock
      print("You can't buy that")
      continue
    elif ship_number == 4:
      break
    #Checks whether you have enough to get the ship
    not_enough = 0
    for i in range(0, 4):
      if items[i] < ship_repair[ship_number][i] and buy_sell == 1:
        print("You don't have enough items")
        not_enough = 1
        break
      elif ship_prices[ship_number] > cash and buy_sell == 0:
        print("You don't have enough cash")
        not_enough = 1
        break
    if not_enough == 1:
      continue
    break
  if buy_sell == 0: #Buying
    cash -= ship_prices[ship_number]
    print("You bought the", available_ships[ship_number])
  elif ship_number != 4: #Fixing the ordinary ships
    for i in range(0, 4):
      items[i] -= ship_repair[ship_number][i]
    print("You fixed the", available_ships[ship_number])
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
  shipname = available_ships[ship_number]
  shipspeed = ship_number + 1
  shiphealth = (ship_number + 1) * 5
  #print(shipname, shipspeed, shiphealth, cash)
  #time.sleep(speed)


days = 0
distance = 0
health = 0
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
  global health
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
  current_repair = random.randint(0, 3) #What the ship currently needs for repair
  repair_amount = random.randint(1, 6 - action_modifier)
  #Initialises 20 events
  #You have a chance at reaching land after day 5
  events = ["You Arrive at Land - Your Journey is Over!",
            "You encounter a Floating Trading Post",
            "You encounter a Floating Trading Post",
            "You encounter a Floating Trading Post",
            "Your ship scrapes the seabed!",
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
  os.system("clear")
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
          print(buildingscost[i][2], itemnames[2], end = " and ")
          print(buildingscost[i][3], itemnames[3], end = ".\n")

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
    elif event in [1, 2, 3]: #Trading Post - shop 
      shop()
    elif event == 4: #Seabed - ship damage
      change = random.randint(1, 7-action_modifier)
      shiphealth -= change
      print(f"You took {change} damage!")
      time.sleep(speed)
    elif event == 5: #Successful Prayer - gives items
      for i in range(0, 6):
        change = random.randint(1, 2+action_modifier)
        items[i] += change
        print("You received", change, itemnames[i], end="!\n")
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
      change = random.randint(1, 7-action_modifier)
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
      change = random.randint(1, 7-action_modifier)
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
      change = random.randint(1, 7-action_modifier)
      health -= change
      print(f"You took {change} damage!")
      time.sleep(speed)
      #Ship Damage
      change = random.randint(1, 8-action_modifier)
      shiphealth -= change
      print(f"Your ship took {change} damage!")
      time.sleep(speed)
    elif event == 18: #Kraken - deals damage to player and ship
      #Player Damage
      change = random.randint(1, 8-action_modifier)
      health -= change
      print(f"You took {change} damage!")
      time.sleep(speed)
      #Ship Damage
      change = random.randint(1, 10-action_modifier)
      shiphealth -= change
      print(f"Your ship took {change} damage!")
      time.sleep(speed)
    elif event == 19: #Rhamnaer and his karambit - deals damage to player and ship
      #Player Damage
      change = random.randint(1, 9-action_modifier)
      health -= change
      print(f"You took {change} damage!")
      time.sleep(speed)
      #Ship Damage
      change = random.randint(1, 11-action_modifier)
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
      return 2
  
    #Calculations Phase
    hunger -= random.randint(5, 10-action_modifier)  #Calculates new hunger value
    if hunger < 0:
      hunger = 0
    
    #Calculates items gained from nets
    changes = [0, 0, 0, 0, 0]
    for i in range(buildings[0]): #Which nets got which stuff
      changes[random.randint(0, 4)] += 1
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
    change = int(random.randint(1, 3+action_modifier) * shipspeed * distance_multiplier)
    distance += change
    print(f"You sailed {change} miles!")
    time.sleep(speed)

    #Separates each day
    print("")
    print("****************************")
    print("")

#Final Score
def final_score(outcome):
  global difficulty
  global distance
  global items
  global speed
  global name
  global shipname
  global days

  difficulties = ["easy", "standard", "hard", "very hard", "extreme"]
  score = 0
  score_mult = 1

  os.system("clear")
  print(f"This was the story of {name}")
  time.sleep(speed)
  print(f"{name} sailed this strange world on their {shipname}!")
  time.sleep(speed)
  print("")
  print(f"It took them {days} days...")
  time.sleep(speed)
  #Gives5000 points if the journey was completed
  if outcome == 0:
    print("And they completed their journey!")
    score += 5000
    time.sleep(speed)
    print("+1000 score")
  if outcome == 1:
    print("But they died along the way!")
  if outcome == 2:
    print(f"But their {shipname} broke!")
  time.sleep(speed)
  print("")
  print(f"Theirs was a {difficulties[difficulty]} journey")
  #Multiplies the final score by (D+1)/2 eg easy is 0.5x modifier and extreme is 3x
  score_mult = (difficulty + 1) / 2
  time.sleep(speed)
  print(f"x{score_mult} Multiplier!")
  time.sleep(speed)
  print("")
  print(f"{name} travelled far")
  time.sleep(speed)
  print(f"Over the course of {days} days...")
  time.sleep(speed)
  #50 Points per day
  score += days * 50
  print(f"+{days * 50} score")
  time.sleep(speed)
  print(f"They travelled {distance} miles")
  time.sleep(speed)
  #10 points per mile travelled
  score += distance * 10
  print(f"+{distance * 10} score")
  time.sleep(speed)
  print("")
  print("Along the way, many items were gathered")
  time.sleep(speed)
  print(f"{items[0]} {itemnames[0]}, {items[1]} {itemnames[1]}, {items[2]} {itemnames[2]}, {items[3]} {itemnames[3]}, {items[4]} {itemnames[4]} and {items[5]} {itemnames[5]}!")
  time.sleep(speed)
  #5 points for every item
  itemsum = sum(items[i] * 5 for i in range(0, 5))
  print(f"+{itemsum} score")
  score += itemsum
  time.sleep(speed)
  print(f"Furthermore, {cash} cash was gathered!")
  #4 points per cash
  score += cash * 4
  print(f"+{cash * 4} score")
  time.sleep(speed)
  print("")
  finalscore = score * score_mult
  print(f"This means a final score of {finalscore}!")
  time.sleep(speed)
  rank = math.floor(math.log10(finalscore / 5))
  #F is not possible but is there to make the other ranks harder to achieve
  #The points necessary are 0, 50, 500, 5000, 50000 and 500000 respectively
  ranks = ["F", "D", "C", "B", "A", "S"]
  print(f"Equivalent to a rank of {ranks[rank]}!")
  time.sleep(speed)
  print("Thanks for playing!")
  time.sleep(speed)
  option = valid_input("Continue (0)? ", 0)
  return int(finalscore)

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

def intro():
  global speed

  #Returning players may not want the explanation
  option = valid_input("Skip Intro (0) or Continue (1)? ", 1)
  if option == 0:
    return
  os.system("clear")

  #This is to take notes on values etc
  print("Before we begin, you may need:")
  time.sleep(speed)
  print(" A Notepad")
  time.sleep(speed)
  print(" A Writing Implement")
  time.sleep(speed)

  #Waits until they want to continue
  option = valid_input("Continue (0)? ", 0)
  os.system("clear")
  time.sleep(speed)

  #Talks about inputs
  print("In this game, you may be asked for input")
  time.sleep(speed)
  print("You have already experienced this")
  time.sleep(speed)
  print("You will be asked to input a number from 0 to X")
  time.sleep(speed)
  print("X will depend on the question")
  time.sleep(speed)
  print("In some cases, this will be obvious")
  time.sleep(speed)
  print("In others, elements of a long list may have been left out for conciseness")
  time.sleep(speed)
  print("This will be denoted with ...")
  time.sleep(speed)
  print("The elements of the list will always have been mentioned")
  time.sleep(speed)
  print("Furthermore, spamming keys may have unintended consequences so please refrain from doing so")
  time.sleep(speed)

  #Waits until they want to continue
  option = valid_input("Continue (0)? ", 0)
  os.system("clear")
  time.sleep(speed)

#A long series of print statements describing the opening moments of the game and assigning the glowing rock on a roughly 1 - 1.04% chance
def opening_story():
  global speed
  global name
  global items
  global action_modifier

  glowing_rock = math.ceil(random.randint(0, 100-action_modifier) / 100)

  if glowing_rock:
    items[-1] = 0
  else:
    items[-1] = 1

  print("You wake up...")
  time.sleep(speed)
  print(f"You are {name}: a legend back in your world")
  time.sleep(speed)
  print("Yet here, you are nothing")
  time.sleep(speed)
  print("You don't know how you got here")
  time.sleep(speed)
  print("Yet something is strangely familiar")
  time.sleep(speed)
  print("As surely as Eleuxaos is good and Rhamnaer is evil, you know where to go")
  time.sleep(speed)
  print("And so you go...")
  time.sleep(speed)
  option = valid_input("Continue (0)? ", 0)
  os.system("clear")

  print("It is not long until you reach a village")
  time.sleep(speed)
  print("Yet this is hardly a village")
  time.sleep(speed)
  print("It is almost dead")
  time.sleep(speed)
  print("There is no hustle and bustle")
  time.sleep(speed)
  print("Buildings lie in ruin")
  time.sleep(speed)
  print("What once must've been a floundering hub of civilisation")
  time.sleep(speed)
  print("Is now a necropolis")
  time.sleep(speed)
  print("You know you need to leave as soon as possible...")
  time.sleep(speed)
  option = valid_input("Continue (0)? ", 0)
  os.system("clear")

  if not glowing_rock:
    print("While wandering, you notice a prescence")
    time.sleep(speed)
    print("In your pocket is located a glowing rock")
    time.sleep(speed)
    print("You feel this could come in handy...")
    time.sleep(speed)
    option = valid_input("Continue (0)? ", 0)
    os.system("clear")
  
  print("You notice a few buildings gathered around the port")
  time.sleep(speed)
  print("While not attractive by any measure, they are inhabited")
  time.sleep(speed)
  print("You come across a worn-down shop")
  time.sleep(speed)
  print("You decide this is your best course of action...")
  time.sleep(speed)
  option = valid_input("Continue (0)? ", 0)
  os.system("clear")

#A shorter series of print statements to provide a short story in the shop-shipyard transition
def shop_to_shipyard():
  global speed

  os.system("clear")
  
  print("Having acquired what you needed for the journey, you look around")
  time.sleep(speed)
  print("You realise that a naval vessel is your only means of escape")
  time.sleep(speed)
  print("You make your way down to the shipyard...")
  option = valid_input("Continue (0)? ", 0)
  time.sleep(speed)

#Gameplay loop
def main():
  setup()
  intro()
  opening_story()
  shop()
  shipyard()
  final_score(journey())

main()
