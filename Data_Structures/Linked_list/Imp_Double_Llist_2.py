# Implement a Doubly-Linked List in python.
# Add methods, such as append, prepend, insert, remove, and print.

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_llist():

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def printList(self):
        arr = []
        current_node = self.head
        while current_node != None:
            arr.append(current_node.data)
            current_node = current_node.next
        return arr

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.append(data)
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    def traverse(self, index):
        count = 0
        current_node = self.head
        while count < index:
            current_node = current_node.next
            count += 1
        return current_node

    def insert(self, data, index):
        new_node = Node(data)
        if index == 0:
            self.prepend(data)
            return
        if index >= self.length:
            self.append(data)
            return
        leader = self.traverse(index - 1)
        follower = leader.next 
        leader.next = new_node
        new_node.prev = leader
        new_node.next = follower
        follower.prev = new_node
        self.length += 1
    
    def remove(self, index):
        if index >= self.length:
            print("Error: Index out of Range.")
            return
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return
        if index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return 
        leader = self.traverse(index - 1)
        temp = leader.next
        follower = temp.next
        leader.next = follower
        follower.prev = leader
        self.length -= 1

l = Doubly_llist()
l.append(5)
l.prepend(6)
l.append(7)
l.append(2)
l.insert(1, 4)
print(l.printList())

    
