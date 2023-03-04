# Implement a Hash Table in python.
# Add methods, such as append, prepend, insert, remove, reverse, and print.

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None


class Linked_list():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        arr = []
        current_node = self.head
        while current_node != None:
            arr.append(current_node.data)
            current_node = current_node.next
        return arr

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    def traverse(self, index):
        count = 0
        current_node = self.head
        while count < index:
            current_node = current_node.next
            count += 1
        return current_node

    
    def insert(self, data, index):
        if index >= self.length:
            self.append(data)
            return
        if index == 0:
            self.prepend(data)
            return
        node = Node()
        leader = self.traverse(index - 1)
        temp = leader.next
        leader.next = node
        node.next = temp
        self.length += 1

    def remove(self, index):
        if index >= self.length:
            print("Error: Index out of Range.")
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        leader = self.traverse(index - 1)
        temp = leader.next
        leader.next = temp.next
        self.length -= 1

    def reverse(self):
        prev = None
        self.tail = self.head
        while self.head != None:
            temp = self.head
            self.head = self.head.next
            temp.next = prev
            prev = temp
        self.head = temp
        






l = Linked_list()
l.append(5)
l.prepend(8)
l.insert(6, 0)
l.remove(5)
print(l.print_list())
l.reverse()
print(l.print_list())