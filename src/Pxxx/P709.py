from src.Pxxx._PluginErrorSuperClass import Squash
from src.Pxxx._PluginErrorSuperClass import PluginError

class P709(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P709"
        self._Text = "Function game is missing"


    def run(self):
        """
        Checks that the function game exists
        """
        try:
            if "game" in dir(Squash):
                self.success()
            else:
                self.fail()
        except Exception as e:
            print(f"{self._Code} Test Aborted due to unexpected error")
            print(e)
            self.fail()
