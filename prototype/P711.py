"""
Checks each data item is a number
"""

import Squash
from _PluginErrorSuperClass import PluginError

class P711(PluginError):

    def __init__(self, reportHere):
        super().__init__(reportHere)
        self._Code = "P711"
        self._Text = "Each item in the Tuple should be a number"

    def run(self):
        try:
            data = Squash.readCSV("data.csv")
            for row in data:
                for item in row:
                    if item.isType("Float") or item.isType("Integer"):
                        # skip
                        pass
                    else:
                        self.fail()
                        return
            self.success()
        except Exception as e:
            print(f"{self._Code} Test Aborted due to unexpected error")
            print(e)
            self.fail()
