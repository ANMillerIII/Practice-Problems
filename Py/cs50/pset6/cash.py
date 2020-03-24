# returns number of coins to give change
import math
from cs50 import get_float

# get input

while True:
    cash = get_float("Cash? ")
    if cash >= 0:
        break
cents = int(math.ceil(cash*100))

# function which determines number of coins


def numCoins(cents):
    change = 0
    while cents > 0:
        if cents - 25 >= 0:
            cents -= 25
            change += 1
        elif cents - 10 >= 0:
            cents -= 10
            change += 1
        elif cents - 5 >= 0:
            cents -= 5
            change += 1
        elif cents - 1 >= 0:
            cents -= 1
            change += 1
    return change


# call function
changed = numCoins(cents)
print(f"{changed}")