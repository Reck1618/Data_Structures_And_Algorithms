# Implement a binary search tree.
# Implement methods, such as insert, lookup, and remove.

class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree():

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

    def print_tree(self):
        if self.root != None:
            return self.__Inorder(self.root)

    # Private Method
    def __Inorder(self, current_node, l = None):
        if l is None:
            l = []

        if current_node != None:
            self.__Inorder(current_node.left, l)
            l.append(current_node.data)
            self.__Inorder(current_node.right, l)
        return l

    def remove(self, data):
        return

x = BinarySearchTree()
x.insert(9)
x.insert(4)
x.insert(6)
x.insert(20)
x.insert(170)
x.insert(15)
x.insert(1)
print(x.lookup(7))
print(x.print_tree())