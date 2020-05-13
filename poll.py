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

from math import sqrt


CONFIDENCE95_COEF = 1.96
CONFIDENCE99_COEF = 2.58


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

    def confidence(self, coef, percentage) -> None:

        """
        Compute and print the 'percentage' confidence interval amplitude.
        """

        confidence = coef * sqrt(self._variance) * 100
        lowestConfidence = 0 if self._p - confidence < 0 else self._p - confidence
        HighestConfidence = 100 if self._p + confidence > 100 else self._p + confidence

        print("{}% confidence interval: [{:.2f}%; {:.2f}%]".format(percentage,
                                                                    lowestConfidence,
                                                                    HighestConfidence))

    def run(self) -> None:

        """
        Run computations and process output printing.
        """

        self.showInputInfomations()
        self.variance()
        self.confidence(CONFIDENCE95_COEF, 95)
        self.confidence(CONFIDENCE99_COEF, 99)
