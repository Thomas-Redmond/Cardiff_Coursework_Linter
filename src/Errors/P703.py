from src.Errors.errorType import basicError

class P703(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self.errorCode = "P703"
        self.errorText = "winProbability must return a number"


    def run(self, Squash):
        """
        Tests that winProbability returns an integer, float or complex value
        """
        try:
            variableReturned = Squash.winProbability(2, 1)
            if isinstance(variableReturned, (int, float, complex)):
                self.success()
            else:
                self.fail()

        except Exception as e:
            print(e)
            self.fail()
