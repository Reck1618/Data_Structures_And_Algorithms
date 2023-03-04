# Implement a Undirected, Unweighted, Graph.

class Graph:

    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentNodes = {}

    def add_Node(self, node):
        self.adjacentNodes[node] = []
        self.numberOfNodes += 1

    def add_Edge(self, node1, node2):
        self.adjacentNodes[node1].append(node2)
        self.adjacentNodes[node2].append(node1)

    def show_connection(self):
        for x in self.adjacentNodes:
            print(x, "-->", self.adjacentNodes[x])

x = Graph()
x.add_Node(0)
x.add_Node(1)
x.add_Node(2)
x.add_Node(3)
x.add_Edge(0, 2)
x.add_Edge(2, 1)
x.add_Edge(2, 3)
x.add_Edge(1, 3)
x.show_connection()