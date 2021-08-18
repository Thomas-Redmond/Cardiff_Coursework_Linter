import ast
from src.Axxx.P700 import P700
from src.Axxx.P701 import P701
from src.Axxx.P702 import P702
from src.Axxx.P705 import P705
from src.Axxx.P713 import P713
from src.Axxx.P714 import P714
from src.Axxx.P717 import P717
from src.Axxx.P716 import P716
from src.Axxx.P718 import P718


class Router(ast.NodeVisitor):

    def __init__(self, errorReporter):
        # Takes instance of Error_Reporter passed by reference
        # To pass information by reference at later stages
        self._reportHere = errorReporter

    def visit_FunctionDef(self, node):
        if node.name == 'game':
            P700_runTest = P700(self._reportHere, node)

        elif node.name == 'q1a':
            P702_runTest = P702(self._reportHere, node)

        elif node.name == 'readCSV':
            P705_runTest = P705(self._reportHere, node)

        elif node.name == 'plotWinProbabilities':
            P713_runTest = P713(self._reportHere, node)
            P714_runTest = P714(self._reportHere, node)
            P716_runTest = P716(self._reportHere, node)
            P718_runTest = P718(self._reportHere, node)

        elif node.name == 'winProbability':
            P701_runTest = P701(self._reportHere, node)
            P717_runTest = P717(self._reportHere, node)

        else:
            pass
        self.generic_visit(node)
