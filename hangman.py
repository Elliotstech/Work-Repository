#Art--- The art printed for the game.
art = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+

  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  
  O   |
 /|\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]


#Define variables
wordlist =["funky", "newbie", "could", "should", "howdy", "blood", "death", "legit", "moose", "goose", "loose", "fluff", "your", "mom"] # --- The possible words for the game.
alphabet = "abcdefghijklmnopqrstuvwxyz" # --- The Alphabet.

import random # --- Importing a module thats used for Randomizing stuff.

def getRandomWord(wordlist):
    secretword = wordlist[random.randint(0,len(wordlist)-1)]
    print ("secretword is", secretword)
    return secretword


#This board prints when you load in
def board(secretword, correctletters, incorrectletters): # --- Defines the function "board"
    print("----------------------------------")
    print("Welcome to The Python Hangman Game")
    print("----------------------------------")
    print(art[len(incorrectletters)])
    
    print("Incorrect letters: ") # --- Listing Incorrect Letters
    for char in incorrectletters: # --- Prints every incorrectly guessed letter.
        print(char,end=" ") 
    print("\nCorrect Letters: ") # --- Listing Correct letters
    blanks = "_" * len(secretword) # --- Calculating the amount of underscores in a word.
#Printing out the blanks
    for index in range(len(secretword)):  # --- Prints the blanks.
        if secretword[index] in correctletters: 
            blanks = blanks[:index] + secretword[index] + blanks[index + 1:]
            print(blanks)  
          
#Error codes
def getguess(alreadyguessed): # --- Defining get guess as an input
    while True:
        guess = input("\nGuess a letter: ")
        if len(guess) > 0:   # --- Keeps the length of the word to be 0
            if guess in alreadyguessed:
                print("That letter has already been guessed. Please try again.") # --- Message displayed when a letter has already been guessed.
            elif guess not in alphabet:
                print("Numbers and punctuation do not work here pleae enter a letter: ") # --- When the user inputs a invalid character.
            else:
                return guess

#Reset
secretword = getRandomWord(wordlist)            
blanks = "_" * len(secretword)  
correctletters = ""
incorrectletters = ""
running = True



while running == True:
    board(secretword, correctletters, incorrectletters)
    guess = getguess(correctletters + incorrectletters)
    if guess in secretword:
        correctletters = correctletters + guess
        foundword = True
        for letter in range(len(secretword)):
            if secretword[letter] not in correctletters: 
                foundword = False # --- This determines if all letters are correct.
        if foundword == True:
            print("You have avoided capital punishment.") # --- The message if you win.
            replay = input("Do you want to play again? ") # --- Asking you if you want to play again.
            if replay == "no" or replay == "No": # --- Telling the computer what response should stop the game.
                running = False
                print ("I don't see you")
            else:
                print ("I see you")
                running = True
                correctletters = ""
                incorrectletters = ""
                secretword = getRandomWord(wordlist)
                blanks = "_" * len(secretword)

    else:
        incorrectletters = incorrectletters + guess
        if len(incorrectletters) == 6: # --- Setting the amount of letters you can get wrong.
            board(secretword, correctletters, incorrectletters)
            print("The game is over you have been hanged.") # --- Game Ended Message
            running = False
            


