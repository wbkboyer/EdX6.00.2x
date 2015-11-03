import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def tallyVowels(wordList):
    vowelCounts = []
    for word in wordList:
        vowelCount = 0.0
        for character in word:
            if character in ['a', 'e', 'i', 'o', 'u']:
                vowelCount += 1
        vowelCounts.append(vowelCount)

    return vowelCounts


def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowelProportions = [y/len(x) for x, y in zip(wordList, tallyVowels(wordList))]

    pylab.hist(vowelProportions, bins = numBins)
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    print 'x-range =', xmin, '-', xmax
    print 'y-range =', ymin, '-', ymax
    pylab.figure
    pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
