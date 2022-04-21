import random, time

#############
#Question 1
###############

while True:

  nouns = ['rice', 'emeka', 'john']
  verbs = ['is', 'goes', 'eats']
  adverbs = ['widely', 'quickly', 'slowly']

  inputt = input("would you like to listen to a unique story (y/n): ")
  
  if inputt == 'y':
    time.sleep(2)
    print()
    print(f"{random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)} known")
    print()
    
  elif inputt == 'n':
    break
    
  else:
    continue

