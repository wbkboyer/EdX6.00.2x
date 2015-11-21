import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """

    pylab.hist(values, bins=numBins)
    if title is not None:
        pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls, and the 95% confidence interval.
        Rounds the mean and confidence interval to 3 decimal places.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    results = []
    for i in range(numTrials):
        prevRoll = None
        longestRun = 1
        currentRun = 1
        for j in range(numRolls):
            roll = int(die.roll())

            if roll == prevRoll:
                currentRun += 1
                if currentRun > longestRun:
                    longestRun = currentRun
            else:
                currentRun = 1

            prevRoll = roll

        results.append(float(longestRun))

    mean, std = getMeanAndStd(results)

    makeHistogram(results, 10, 'Longest Roll Length', 'Num. Trials with Roll Length', title='Frequency of Roll Lengths')

    return round(mean,4)


    
# One test case
print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)

# print getAverage(Die([1]), 10, 1000)
# print getAverage(Die([1,1]), 10, 1000)
# print getAverage(Die([1,2,3,4,5,6]), 50, 1000)
# print getAverage(Die([1,2,3,4,5,6,6,6,7]), 50, 1000)
# print getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000)
