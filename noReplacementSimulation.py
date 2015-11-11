import random

def drawBall(balls):
    return random.choice(balls)

def drawBalls(numRedBalls, numGreenBalls, numBallsToBeDrawn):
    balls = []
    for i in range(numRedBalls):
        balls.append('r')
    for i in range(numGreenBalls):
        balls.append('g')

    redBallsDrawn = 0
    greenBallsDrawn = 0
    for i in range(numBallsToBeDrawn):
        choice = drawBall(balls)
        if choice == 'r':
            redBallsDrawn +=1
            balls.remove('r')
        if choice == 'g':
            greenBallsDrawn += 1
            balls.remove('g')

    if redBallsDrawn == 3 or greenBallsDrawn == 3:
        return 1.0

    return 0


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''

    sameColourDrawn = 0.0
    for i in range(numTrials):
        sameColourDrawn += drawBalls(3, 3, 3)

    return sameColourDrawn/numTrials

if __name__ == '__main__':
    #for i in range(10):
    print(noReplacementSimulation(5000))


