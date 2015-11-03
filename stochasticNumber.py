__author__ = 'wbkboyer'

import random

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''

    evens = [x for x in range(9, 21) if x%2 is 0]
    return random.choice(evens)


if __name__ == "__main__":
    print(stochasticNumber())
