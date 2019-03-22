# Import modules
import time
import random

# Print credits
print('Created by Serentex (Ryan Buchanan), Elliot Murray, and James Blackburn.')
print('Using version 6.')

# Define variables
wrong = 0
totalWrong = 0
totalCorrect = 0
playGame = True

try:
    while(playGame):
        try:
            number = int(input('Enter a number between 1-100: '))
            if(number > 100): #--- If user number was higher than 100
                print('Number was higher than 100. Defaulting to 50.')
                number = 50
            elif(number < 1): #--- If user number is less than 1
                print('Number was lower than 1. Defaulting to 50.')
                number = 50
            else:
                print
            guess = random.randint(1, 100)
            while(guess != number):
                wrong += 1
                time.sleep(0.5)
                print('The computer guessed', guess)
                print('Computer guessed wrong. Guessing again.')
                if(guess > number):
                    if(guess < 1):
                        guess = 1
                    elif(guess > 100):
                        guess = 100
                    else:
                        guess = random.randint(number, guess)
                elif(guess < number):
                    if(guess < 1):
                        guess = 1
                    elif(guess > 100):
                        guess = 100
                    else:
                        guess = random.randint(guess, number)
            if(guess == number):
                totalWrong += wrong
                totalCorrect += 1
                print('The computer guessed your number.')
                print('The computer guessed', wrong, 'times before guessing correctly.')
                print('The computer has guessed incorrectly', totalWrong, 'times since startup.')
                print('The computer has guessed correctly', totalCorrect, 'times since startup.')
            answer = input('Do you want to play again? ')
            if(answer == 'yes' or answer == 'Yes'):
                wrong = 0
            elif(answer == 'no' or answer == 'No'):
                playGame = False


        except ValueError: #---Value Error 
            number = 50
            print('Invalid input. Defaulting to 50.')
            guess = random.randint(1, 100)
            while(guess != number):
                wrong += 1
                time.sleep(0.5)
                print('The computer guessed', guess)
                print('Computer guessed wrong. Guessing again.')
                if(guess > number):
                    if(guess < 1):
                        guess = 1
                    elif(guess > 100):
                        guess = 100
                    else:
                        guess = guess - random.randint(number, guess)
                elif(guess < number):
                    if(guess < 1):
                        guess = 1
                    elif(guess > 100):
                        guess = 100
                    else:
                        guess = guess + random.randint(guess, number)
            if(guess == number):
                totalWrong += wrong
                print('The computer guessed your number.')
                print('The computer guessed', wrong, 'times before guessing correctly.')
                print('The computer has guessed incorrectly', totalWrong, 'times since startup.')
                print('The computer has guessed correctly', totalCorrect, 'times since startup.')
            answer = input('Do you want to play again? ')
            if(answer == 'yes' or answer == 'Yes'):
                wrong = 0
            elif(answer == 'no' or answer == 'No'):
                playGame = False

except KeyboardInterrupt:
    print('\nProgram stopped using Ctrl+C.')
