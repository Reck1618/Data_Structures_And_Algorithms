# Implement Depth First Search. 

class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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

    def lookup(self, data):
        current_node = self.root
        while True:
            if not current_node:
                return False
            elif current_node.data == data:
                return True
            elif data > current_node.data:
                current_node = current_node.right
            else:
                current_node = current_node.left

    def inorder_traversal(self):
        return self.__Inorder(self.root)

    def postorder_traversal(self):
        return self.__Postorder(self.root)

    def preorder_traversal(self):
        return self.__Preorder(self.root)
    
    def __Inorder(self, current_node, visited_node = None):
        if visited_node is None:
            visited_node = []

        if current_node:
            self.__Inorder(current_node.left, visited_node)
            visited_node.append(current_node.data)
            self.__Inorder(current_node.right, visited_node)

        return visited_node 
        
    def __Postorder(self, current_node, visited_node = None):
        if visited_node is None:
            visited_node = []

        if current_node:
            self.__Postorder(current_node.left, visited_node)
            self.__Postorder(current_node.right, visited_node)
            visited_node.append(current_node.data)

        return visited_node

    def __Preorder(self, current_node, visited_node = None):
        if visited_node is None:
            visited_node = []

        if current_node:
            visited_node.append(current_node.data)
            current_node.data
            self.__Preorder(current_node.left, visited_node)
            self.__Preorder(current_node.right, visited_node)
        
        return visited_node
    

#      5
#   3     7
# 2   4 6   9

# Demo Run
x = Binary_Tree()       
for i in [5,3,7,2,4,6,9]: 
    x.insert(i)
print(*x.inorder_traversal())
print(*x.postorder_traversal())
print(*x.preorder_traversal())
