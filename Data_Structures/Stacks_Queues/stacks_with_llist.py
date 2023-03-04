# Implement a stack, built with linked lists. 
# Add methods such as peek, push, and pop.

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def printStack(self):
        arr = []
        temp = self.top
        while self.top != None:
            arr.append(self.top.data)
            self.top = self.top.next
        return arr
    
    def peek(self):
        return self.top.data
    
    def push(self, data):
        new_node = Node(data)
        if self.bottom == None:
            self.bottom = new_node
            self.top = self.bottom
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
       
    def pop(self):
        if not self.top:
            return None
        if self.top == self.bottom:
            self.bottom = None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -= 1
        return temp.data
 

x = Stack()
x.push("youtube")
x.push("hello")
print(x.pop())
print(x.printStack())

    
