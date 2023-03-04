# Implement a Linked List in python.
# Add methods, such as append, prepend, insert, remove, reverse, and print.
class Linked_list():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):                    
        return str(self.__dict__)

    def append(self,data):
        new_node = {"value": data, "next": None} 
        if self.head == None:              
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            self.tail["next"] = new_node
            self.tail =  new_node
            self.length += 1

        return self.printList()
    
    def prepend(self,data):
        new_node = {"value": data, "next": None}               
        new_node["next"] = self.head
        self.head = new_node
        self.length += 1
        
        return self.printList()


    def insert(self, data, index):
        if index >= self.length:
            return self.append(data)
        if index == 0:
            return self.prepend(data)
        
        new_node = {"value": data, "next": None}
        leader = self.traverse(index-1)
        temp = leader["next"]
        leader["next"] = new_node
        new_node["next"] = temp
        self.length +=1

        return self.printList()

    def traverse(self,index):
        count = 0
        current_node = self.head
        while count < index:
            current_node = current_node["next"]
            count += 1
        return current_node

    def remove(self,index):
        if index >= self.length:
            print("Index out of Range")
        if index == 0:
            self.head = self.head["next"]
            self.length -= 1
            return self.printList()

        leader = self.traverse(index - 1)
        temp = leader["next"]
        leader["next"] = temp["next"]
        self.length -= 1
        return self.printList()

    def reverse(self):
        prev = None
        self.tail = self.head
        while self.head != None:
            temp = self.head
            self.head = self.head["next"]
            temp["next"] = prev
            prev = temp
        self.head = temp 
        return self.printList()

    def printList(self):
        arr = []
        current_node = self.head
        while current_node != None:
            arr.append(current_node["value"])
            current_node = current_node["next"]
        return arr

l = Linked_list()
print(l.append(5))
print(l.insert(1, 0))
print(l.remove(0))
print(l)
