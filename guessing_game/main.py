import random
import math


#take inputs for the range the computer is to generate a number
lower_bound = int(input('Enter lower bound of range:- '))
upper_bound = int(input('Enter upper bound of range:- '))

count = 0 #count number of guesses made
MAX_GUESSES = 6 #Maximum number of guesses
won = False


#generate random number
def generateRandomNum():
    random_number = random.randint(lower_bound, upper_bound)
    return random_number

#check guess against random number
def checkGuesses(random_number):
    global count
    global won

    while(count < MAX_GUESSES or won):
        guess = int(input('Guess a number:- '))
        count += 1
        
        if guess == random_number:
            print('Congratulations, you guessed it in ', count, ' tries!')
            won = True
        elif guess < random_number:
            print('You guessed too small!')
        elif guess > random_number:
            print('You guessed too high!')    

random_number = generateRandomNum()
checkGuesses(random_number)