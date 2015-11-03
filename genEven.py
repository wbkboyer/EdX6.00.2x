__author__ = 'wbkboyer'

import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    evens = [x for x in range(100) if x%2 is 0]
    return random.choice(evens)

if __name__ == "__main__":
    print(genEven())