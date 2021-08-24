from Errors.errorType import basicError

class P711(basicError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._errorCode = "P711"
        self._errorText = "Each item returned in the Tuple should be a number"

    def run(self, Squash):
        """
        Checks that each item returned by Squash.readCSV is a number
        """
        try:

            data = Squash.readCSV("test.csv")
            for row in data:
                for item in row:
                    if isinstance(item, (int, float, complex)):
                        pass
                    else:
                        self.fail()
                        return
                self.success()

        except Exception as e:
            print(e)
            self.fail()
