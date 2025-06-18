from _tree_graph import TreeGraph
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
X, y = iris.data, iris.target
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

import graphviz
dot_data = tree.export_graphviz(
    clf, out_file=None, label="none", proportion=False, impurity=False
)
graph = graphviz.Source(dot_data)
graph.render("iris")

treeGraph = TreeGraph(dot_data)

print(dot_data)

nodes = treeGraph.Nodes
edges = treeGraph.Edges
leaves = treeGraph.Leaves

# Example of manipulating a node
node = nodes[5]
print(node)
node.set_label(f"Test")
print(node)

# new_dot_data = treeGraph.export()
# print(new_dot_data)
# new_graph = graphviz.Source(new_dot_data)
# new_graph.render("iris2")
