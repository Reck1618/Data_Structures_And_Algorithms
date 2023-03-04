# Some improvement made to DFS by Trincot_stackoverflow.

class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def traverse(self, order=0):
        if order == -1:
            yield self.data
        if self.left:
            yield from self.left.traverse(order)
        if order == 0:
            yield self.data
        if self.right:
            yield from self.right.traverse(order)
        if order == 1:
            yield self.data
        

class Binary_Tree():

    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if data > current_node.data:
                    if not current_node.right:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right
                else:
                    if not current_node.left:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
    
    def preorder_traversal(self):
        if self.root:
            return self.root.traverse(-1)

    def inorder_traversal(self):
        if self.root:
            return self.root.traverse(0)
    
    def postorder_traversal(self):
        if self.root:
            return self.root.traverse(1)
    
# Demo run
tree = Binary_Tree()
for data in range(10):
    tree.insert(data)
print(*tree.inorder_traversal())