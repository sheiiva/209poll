############################################
#                MATHEMATICS               #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#           Project : 209poll_2019         #
#                                          #
############################################


class ArgumentManager():

    def checkArgs(self, argv) -> int:

        """
        Check for arguments validity.
        """

        def isInt(value) -> bool:
            try:
                int(value)
            except ValueError:
                return False
            else:
                return True

        def isFloat(value) -> bool:
            try:
                float(value)
            except ValueError:
                return False
            else:
                return True

        if len(argv) != 4:
            print("Wrong number of arguments. Please retry with -h.")
            return 84
        if not isInt(argv[1]) or not isInt(argv[2]) or not isFloat(argv[3]):
            print("Wrong argument type. Please retry with -h.")
            return 84
        elif int(argv[2]) >= int(argv[1]):
            print("Size of the sample might be smaller than the size of the population. Please retry with -h.")
            return 84
        elif int(argv[1]) <= 0 or int(argv[2]) <= 0:
            print("Wrong value. Please retry with -h.")
            return 84
        elif float(argv[3]) < 0.0 or float(argv[3]) > 100.0:
            print("Wrong value. Please retry with -h.")
            return 84

        return 0

    def needHelp(self, argv) -> bool:

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
