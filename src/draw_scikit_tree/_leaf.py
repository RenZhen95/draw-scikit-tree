class Leaf:
    '''
    Class to represent a leaf.

    Parameters
    ----------
    line : str
     - Line from DOT script

    Attributes
    ----------

    '''
    def __init__(self, line):
        self.line = line

    def __str__(self):
        _printOut = f"=== === ===\nLeaf :: {self.line}\n--- --- ---\n"

        return _printOut
