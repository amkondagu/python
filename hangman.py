tries = '' #set tries to no value
word = input("select a word: ") #set the secret word
mylist = [] #empty list for the users progress
correct = 0 #the user has not answered correct yet
pastguesses = [] #empty list to save past guesses

def asktries():
  global tries
  while True: #repeat forever
    tries = (input("how many tries do you want? ")) #ask user for how many wrong guesses they want
    try: 
      tries = int(tries)
    except: #if there is an error:
      print("please write an integer")
      print('')
      continue
    if tries < 1:
      print("")
      print("the number of tries must be greater than 0")
    elif tries > 25:
      print("")
      print("tries must be smaller than 26")
    else:
      break

asktries()

for i in range(len(word)): #repeat for how many letters are in the word
  mylist.append('*') #add a star to the list
  
wordlen = len(mylist) #you need to get this many letters right to win
 
while True: #forever loop
  print('') #add a line of space
  print("word: ", *mylist) #show the user their progress
  if tries == 1: 
    print("you have", tries, "try left")
  else:
    print("you have", tries, "tries left")
  print("pastguesses: ", *pastguesses) #show the user their previous guesses
  loop = -1 #reset number of loop
  guesses = str(input("guess: ")) #ask the user for their guess
  
  while len(guesses) > 1: #repeat until the user only writes one letter
    print("only one letter")
    guesses = input("guess again ")
  
  if guesses in pastguesses: 
    print("you already guessed that")
    continue
  
  tries -= 1 #remove a try
  
  for char in word: #repeat for every letter in the word
    loop += 1
    if char in guesses: #if you guessed correctly
      correct += 1 #add one to the number of correct guesses
      mylist[loop] = char #update your progress
 
  if guesses not in word: 
    print(guesses, "is not in the word")
    
  elif guesses in word:
    print(guesses, "is in the word")
    tries += 1 
      
  if correct == wordlen: 
    print("you won!")
    break
  
  elif 0 == tries:
    print("you lose!")
    break
  
  pastguesses.append(guesses)
  
print("the word was", word)
  

