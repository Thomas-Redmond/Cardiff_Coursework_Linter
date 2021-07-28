class PluginError:
    self._Type = "Plugin Error"
    self._Code = ""
    self._Text = ""

    def __init__(self, reportHere):
        self._reportHere = reportHere


    def run(self):
        # Overridden by Child class
        return

    def success(self):
        return

    def fail(self):
        self._reportHere.([0, 0, self._Type + ": " + self._Code + ": " + self._Text])

    def displayAll(self):
        """
        Prints all the data of the class with easy to read display
        """
        print(f'Type: {self._Type}')
        print(f'Code: {self._Code}')
        print(f'Text: {self._Text}')
        return

    def setType(self, Type):
        self._Type = Type
        return

    def getType(self):
        return self._Type

    def setCode(self, Code):
        self._Code = Code
        return

    def getCode(self):
        return self._Code

    def setText(self, Text):
        self._Text = Text
        return

    def getText(self):
        return self._Text
