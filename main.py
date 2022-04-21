import random, time

#############
#Question 1
###############

# while True:

#   nouns = ['rice', 'emeka', 'john']
#   verbs = ['is', 'goes', 'eats']
#   adverbs = ['widely', 'quickly', 'slowly']

#   inputt = input("would you like to listen to a unique story (y/n): ")
  
#   if inputt == 'y':
#     time.sleep(2)
#     print()
#     print(f"{random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)} known")
#     print()
    
#   elif inputt == 'n':
#     break
    
#   else:
#     continue

#############
#Question 2
###############
player = [2, 3, 4, 5, 6, 7, 8, 9, 10]
computer = [2, 3, 4, 5, 6, 7, 8, 9, 10]

player_point = 0
computer_point = 0

while True: 

  #drawing a card from each list
  if len(player) > 0:
    random.shuffle(player)
    choice_list1 = random.choice(player)
    print(f"Random selection from player: {choice_list1}")
    player.remove(choice_list1)
    
    
  if len(computer) > 0:
    random.shuffle(computer)
    choice_list2 = random.choice(computer)
    computer.remove(choice_list2)
    print(f"Random selection from computer : {choice_list2}")  
  print()
  time.sleep(2)

  if choice_list1 > choice_list2:
    print("player has a higher value")
    player_point += 1
    print(f"player point: {player_point}")
    print()
    time.sleep(2)

  if choice_list2 > choice_list1:
    print("computer has a higher value")
    computer_point += 1
    print(f"computer point: {computer_point}")
    print()
    time.sleep(2)  

  if choice_list1 == choice_list2:
    print("There is a WAR\nGame continues")
    print()
    time.sleep(2)
    continue    


  if len(player) == 0 and player_point > computer_point:
    print("Player Wins Game\nGame Ends!")
    break

  if len(player) == 0 and computer_point > player_point:
    print("Computer Wins Game\nGame Ends!")
    break
    
  if len(player) == 0 and computer_point == player_point:
    print("Tie!")
    print()
    time.sleep(2)
    continue
  
  