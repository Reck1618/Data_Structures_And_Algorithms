# Implement BFS in Directed graph.

class Graph:

    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentNodes = {}

    def add_Node(self, node):
        self.adjacentNodes[node] = []
        self.numberOfNodes += 1

    def add_Edge(self, node1, node2):
        self.adjacentNodes[node1].append(node2)

    def show_connection(self):
        for x in self.adjacentNodes:
            print(x, "-->", self.adjacentNodes[x])


    def bfs_traversal(self, node):
        if node in self.adjacentNodes:
            current_node = node 
            queue = []
            visited_node = []

            queue.append(current_node)

            while queue:
                current_node = queue.pop(0)
                if current_node not in visited_node:
                    visited_node.append(current_node)

                for x in self.adjacentNodes[current_node]:
                    if x not in visited_node:
                        queue.append(x)
            
            return visited_node
        return "Enter a valid node."




# Demo Run

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

print(*x.bfs_traversal(5))
