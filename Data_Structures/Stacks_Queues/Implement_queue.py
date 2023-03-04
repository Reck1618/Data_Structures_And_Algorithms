# Implement a queue, built with Linked Lists. 
# Add methods such as peek, enqueue, dequeue, and printQueue.

class Node():

    def __init__(self, data):
        self.data = data 
        self.next = None

    
class Queue():

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.data

    def enqueue(self, data):
        new_node = Node(data)
        if self.first == None:
            self.first = new_node
            self.last = self.first
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        if self.first == None:
            return None
        if self.first == self.last:
            self.last = None
        
        dequeue_ele = self.first
        self.first = self.first.next
        dequeue_ele.next = None
        self.length -= 1
        return dequeue_ele.data

    def printQueue(self):
        array = []
        temp = self.first
        while temp != None:
            array.append(temp.data)
            temp = temp.next
        return array

x = Queue()
x.enqueue("youtube")
x.enqueue("microsoft")
x.enqueue("amazon")
print(x.dequeue())
print(x.printQueue())