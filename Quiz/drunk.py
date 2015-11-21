import pylab

class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]



import random

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)]
        return random.choice(stepChoices)

def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())

def runSimulation(num_drunks, num_steps, num_trials, drunk_type):

    for i in range(num_trials):

        drunks = [] # will be a list of drunks of type drunk_type with a number for a name (they're really drunk)

        # initialize list of drunks of drunk_type
        for j in range(num_drunks):
            drunks.append(drunk_type(str(j)))

        field = Field()
        origin = Location(0.0, 0.0)
        walk_vectors = []
        for drunk in drunks:
            field.addDrunk(drunk, origin)
            #  Move each drunk one step for each iteration of the outer loop, up to num_steps
            walk_vectors.append(walkVector(field, drunk, num_steps))


        for j in range(num_steps):

            for drunk in drunks:
                field.moveDrunk(drunk)



        for drunk in drunks:


    #  Return a collection of actual distances from the origin for a set of trials
    return walk_vectors

def showPlot(num_drunks, num_steps, num_trials):
    """
    What information does the plot produced by this function tell you?
    """
    drunk_types = ['UsualDrunk', 'ColdDrunk', 'EDrunk', 'PhotoDrunk', 'DDrunk']
    list_of_walk_vectors = []
    for drunk_type in drunk_types:
        list_of_walk_vectors.append(runSimulation(num_drunks, 100, 300, drunk_type))

    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)

    pylab.show()