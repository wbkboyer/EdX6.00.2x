import pylab

def readFile ():
    diffTemps = []
    inFile = open('/home/wbkboyer/EdX6.00.2x/Temps/julyTemps.txt', 'r')

    for line in inFile:
        fields = line.split()
        if len(fields) < 3 or fields[0] == 'Boston' or fields[0] == 'Day':
            continue
        else:
            diff = int(fields[1])-int(fields[2])
            diffTemps.append(diff)

    return diffTemps

def producePlot(diffTemps):
    pylab.plot(range(1,32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()


if __name__ == "__main__":
    diffTemps = readFile()
    producePlot(diffTemps)