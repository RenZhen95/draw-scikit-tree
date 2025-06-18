class Node:
    '''
    Class to represent a tree node.

    Parameters
    ----------
    line : str
     - Line from DOT script
    '''
    def __init__(self, line):
        self.line = line
        
        self.ID = self.get_id(self.line)

        self.Feature, self.FeatureThreshold = self.get_feature_threshold(
            self.line
        )

    def get_id(self, line):
        '''Get node's ID'''
        return line.split(" [")[0]

    def __str__(self):
        _printOut = f"=== === ===\nNode :: {self.line}\n--- --- ---\n"

        return _printOut

    def get_feature_threshold(self, line):
        '''Returns the feature name and threshold'''
        linesplits = line.split('\\n')

        f = linesplits[0].split("<=")[0].split("=")[1][1:]
        
        featureSplit = f.split('_')
        f_threshold = linesplits[0].split("<= ")[-1]
        
        return f, f_threshold

    def get_label_content(self):
        '''Internal function to get the contents of the label'''
        self.

    def set_label(self, _input):
        '''Set the label'''
        self.line = _input

        
