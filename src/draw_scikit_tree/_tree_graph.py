from _node import Node
from _edge import Edge
from _leaf import Leaf
from collections import defaultdict

class TreeGraph:
    '''
    Interface to allow for more user-friendly DOT script modifications.

    Parameters
    ----------
    dot_data : str
     - DOT script to generate tree plot
    '''
    def __init__(self, dot_data):
        dot_data = dot_data.splitlines()

        self.line_dict = defaultdict(str)

        # Indicator of a node
        isNode = lambda x: True if " <= " in x else False
        self.Nodes = []

        # Indicator of an edge
        isEdge = lambda x: True if " -> " in x else False
        self.Edges = []

        # Indicator of a leaf
        isLeaf = lambda x: True if " [label=" in x else False
        self.Leaves = []

        for i, line in enumerate(dot_data):
            # Check if line is a node
            if isNode(line):
                self.Nodes.append(Node(line))
                self.line_dict[i] = self.Nodes[-1]

            else:
                # Check if line is an edge
                if isEdge(line):
                    self.Edges.append(Edge(line))
                    self.line_dict[i] = self.Edges[-1]

                # Check if line is a leaf
                elif isLeaf(line):
                    self.Leaves.append(Leaf(line))
                    self.line_dict[i] = self.Leaves[-1]

                # Neither Node, Edge or Leaf
                else:
                    self.line_dict[i] = line

    def export(self):
        '''
        Exports DOT script, including changes made by user to every
        Node, Edge, and Leaf object.
        '''
        new_dot_data = ""
        for k in self.line_dict.keys():
            if isinstance(self.line_dict[k], Node):
                new_dot_data += f"{self.line_dict[k].line}\n"
            elif isinstance(self.line_dict[k], Edge):
                new_dot_data += f"{self.line_dict[k].line}\n"
            elif isinstance(self.line_dict[k], Leaf):
                new_dot_data += f"{self.line_dict[k].line}\n"
            else:
                new_dot_data += f"{self.line_dict[k]}\n"

        return new_dot_data
