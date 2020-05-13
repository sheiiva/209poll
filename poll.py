############################################
#                MATHEMATICS               #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#           Project : 209poll_2019         #
#                                          #
############################################


from sys import argv
import numpy as np


class Poll():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._pSize = int(argv[1])
        self._sSize = int(argv[2])
        self._p = float(argv[3])
        self._variance = 0

    def showInputInfomations(self) -> None:

        def showPopulationSize() -> None:
            
            """
            Print out the population size.
            """

            print("Population size:\t{}".format(self._pSize))

        def showSampleSize() -> None:

            """
            Print out the sample size.
            """

            print("Sample size:\t\t{}".format(self._sSize))

        def showVotingIntentions() -> None:

            """
            Print out the votin intention percentage.
            """

            print("Voting intentions:\t{:.2f}%".format(self._p))

        showPopulationSize()
        showSampleSize()
        showVotingIntentions()

    def variance(self) -> None:

        """
        Compute and print the variance.
        """

        variance = (self._p * (100-self._p)) / 10000
        emean = (self._pSize - self._sSize) / (self._pSize - 1)
        self._variance = (variance / self._sSize) * emean

        print("Variance:\t\t{:.6f}".format(self._variance))

    def run(self) -> None:

        """
        Run computations and process output printing.
        """

        self.showInputInfomations()
        self.variance()