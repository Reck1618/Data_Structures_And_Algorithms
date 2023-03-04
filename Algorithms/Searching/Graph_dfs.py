# Implement DFS In Directed Graph.

class Graph:

    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentNodes = {}

    def add_Node(self, node):
        self.adjacentNodes[node] = []
        self.numberOfNodes += 1

    def add_Edge(self, node1, node2):
        self.adjacentNodes[node1].append(node2)
        #self.adjacentNodes[node2].append(node1)

    def show_connection(self):
        for x in self.adjacentNodes:
            print(x, "-->", self.adjacentNodes[x])

    def dfs_traversal(self, node, visited_node = None):
        if node in self.adjacentNodes:
            if visited_node is None:
                visited_node = []

            visited_node.append(node)

            for x in self.adjacentNodes[node]:
                if x not in visited_node:
                    self.dfs_traversal(x, visited_node)

            return visited_node
        return "Enter a valid node."




array = [5,3,7,2,4,8]
x = Graph()
x.add_Node(5)
x.add_Node(3)
x.add_Node(7)
x.add_Node(2)
x.add_Node(4)
x.add_Node(8)
x.add_Edge(5, 3)
x.add_Edge(5, 7)
x.add_Edge(3, 2)
x.add_Edge(3, 4)
x.add_Edge(7, 8)
x.add_Edge(4, 8)
x.show_connection()
print(*x.dfs_traversal(5))