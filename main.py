### Setup Section ###

from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position 
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if(letter in actual):

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == actual[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:

        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True, False)

    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      printColorfulLetter(letter, False, False)
      
    print(Style.RESET_ALL + " ", end="")

def getSixLetterInput():

# Initialize word string to empty
  word = ""

# Loop until user has entered a 6-letter word
  while (len(word) != 6):
    word = input("Enter a six letter word: ")
  return(word)

def displayTitle():

# print title

  print(r"""
 .----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. |
| | _____  _____ | || |     ____     | || |  _______     | || |  ________    | | | |   ______     | || |   _____      | || |      __      | || |  ____  ____  | |
| ||_   _||_   _|| || |   .'    `.   | || | |_   __ \    | || | |_   ___ `.  | | | |  |_   __ \   | || |  |_   _|     | || |     /  \     | || | |_  _||_  _| | |
| |  | | /\ | |  | || |  /  .--.  \  | || |   | |__) |   | || |   | |   `. \ | | | |    | |__) |  | || |    | |       | || |    / /\ \    | || |   \ \  / /   | |
| |  | |/  \| |  | || |  | |    | |  | || |   |  __ /    | || |   | |    | | | | | |    |  ___/   | || |    | |   _   | || |   / ____ \   | || |    \ \/ /    | |
| |  |   /\   |  | || |  \  `--'  /  | || |  _| |  \ \_  | || |  _| |___.' / | | | |   _| |_      | || |   _| |__/ |  | || | _/ /    \ \_ | || |    _|  |_    | |
| |  |__/  \__|  | || |   `.____.'   | || | |____| |___| | || | |________.'  | | | |  |_____|     | || |  |________|  | || ||____|  |____|| || |   |______|   | |
| |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------' 

""")

def displayWelcomeMsgAndRules():
  print("Welcome to Word Play!")
  print("====================")
  print("You have six tries to get the word correct")
  print("The word is SIX CHARACTERS long, and you must enter a guess of this length")
  print("If a letter is in the correct place, it will be green")
  print("If a letter is in the word but NOT in the correct place, it will be yellow")
  print("If a letter is NOT in the word, it will be red")
  print()

### Main Program ###

# Create Secret Word
secret = "flower"

# Initialize guess string and number of guesses
guess = ""
guessCount = 0

# Display Title
displayTitle()

# Display Welcome message and Rules
displayWelcomeMsgAndRules()

# create loop to prompt user for his/her guesses up to 6 until
while ((guessCount != 6) and (guess != secret)):

# Get user guess
  guess = getSixLetterInput()

# Display color-coded letter results
  printGuessAccuracy(guess, secret)

# print newline for formatting
  print()

# increment the number of guesses
  guessCount += 1

# Display result message

if (guess == secret):
  print("You won!")
else:
  print("Sorry, you lose")