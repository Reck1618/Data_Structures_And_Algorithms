# Implement Binary Search With Recursion. 

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

    def breadth_first_search_r(self):
        if self.root != None:
            return self.__recursive([self.root])

    def __recursive(self, queue, visited_nodes = None):
        if visited_nodes is None:
            visited_nodes = []

        #the input queue must be in a []

        if not queue:
            return visited_nodes
        
        current_node = queue.pop(0)
        visited_nodes.append(current_node.data)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

        return self.__recursive(queue, visited_nodes)
     

#      5
#   3     7
# 2   4 6   9

#Demo Run
x = Binary_Tree()       
for i in [5,3,7,2,4,6,9]:
    x.insert(i)
print(*x.breadth_first_search_r())