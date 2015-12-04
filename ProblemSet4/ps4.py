# 6.00.2x Problem Set 4

import numpy
import random
import pylab
import matplotlib.pyplot as plt
from ps3b import *

#
# PROBLEM 1
#

def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)

    Use the following parameters to initialize a TreatedPatient:

    - viruses, a list of 100 ResistantVirus instances

    - maxPop, maximum sustainable virus population = 1000

    Each ResistantVirus instance in the viruses list should be initialized with the following parameters:

    - maxBirthProb, maximum reproduction probability for a virus particle = 0.1

    - clearProb, maximum clearance probability for a virus particle = 0.05

    - resistances, The virus's genetic resistance to drugs in the experiment = {'guttagonol': False}

    - mutProb, probability of a mutation in a virus particle's offspring = 0.005

    Rather than averaging the final virus population across different trials as in the last pset,
    this time use pylab's hist() function to plot a histogram of the final virus populations under
    each condition for each trial.

    You may also find pylab's subplot function to be helpful.

    The x-axis of the histogram should be the final total virus population values (choose x axis
    increments or "histogram bins" according to the range of final virus population values you get
    by running the simulation multiple times). Then, the y-axis of the histogram should be the number
    of trials belonging to each histogram bin. You should decide the number of trials you ran for
    each condition in order to obtain a reasonable distribution
    """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005

    f, axarr = plt.subplots(4)
    plotNum = 0
    for adminTime in [300, 150, 75, 0]:
        finalPops = []
        for i in range(numTrials):
            viruses = []
            for j in range(numViruses):
                viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))

            patient = TreatedPatient(viruses, maxPop)

            for k in range(1, (adminTime+1)+150):
                if k == adminTime:
                    patient.addPrescription('guttagonol')
                patient.update()

            finalPops.append(patient.getTotalPop())

        axarr[plotNum].hist(finalPops, bins=30)
        axarr[plotNum].set_title("Simulation with Drug administered after "+str(adminTime)+" steps.")

        plotNum += 1
    plt.xlabel('num virus left')
    plt.ylabel('how many trials')
    plt.show()


# simulationDelayedTreatment(100)



#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).
    """

    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.05

    f, axarr = plt.subplots(4)
    plotNum = 0
    for adminTime in [300, 150, 75, 0]:
        finalPops = []
        for i in range(numTrials):
            viruses = []
            for j in range(numViruses):
                viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))

            patient = TreatedPatient(viruses, maxPop)

            for k in range(1, 150+(adminTime+1)+150):
                if k == 150:
                    patient.addPrescription('guttagonol')
                if k == 150 + adminTime:
                    patient.addPrescription('grimpex')
                patient.update()

            finalPops.append(patient.getTotalPop())

        axarr[plotNum].hist(finalPops, bins=30)
        axarr[plotNum].set_title("Simulation with Drug administered after "+str(adminTime)+" steps.")

        plotNum += 1
    plt.xlabel('num. virus left')
    plt.ylabel('how many trials?')
    plt.show()



simulationTwoDrugsDelayedTreatment(30)