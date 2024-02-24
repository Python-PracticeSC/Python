import random
import math

#take inputs for the range the computer is to generate a number
lower_bound = int(input('Enter lower bound of range:- '))

upper_bound = int(input('Enter upper bound of range:- '))

#count number of guesses made
count = 0

#generate random number
def generateRandomNum():
    random_number = random.randint(lower_bound, upper_bound)
    return random_number

print(generateRandomNum())