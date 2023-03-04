# Implement a Doubly-Linked List in python.
# Add methods, such as append, prepend, insert, remove, and print.
class Doubly_llist():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):                    
        return str(self.__dict__)

    def append(self,data):
        new_node = {"value": data, "next": None, "prev": None} 
        if self.head == None:              
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node["prev"] = self.tail
            self.tail["next"] = new_node
            self.tail =  new_node
            self.length += 1

        return self.printList()
    
    def prepend(self,data):
        new_node = {"value": data, "next": None, "prev": None}
        if self.head == None:
            self.append(data)
        else:        
            new_node["next"] = self.head
            self.head["prev"] = new_node 
            self.head = new_node
            self.length += 1
        
        return self.printList()

    def printList(self):
        arr = []
        current_node = self.head
        while current_node != None:
            arr.append(current_node["value"])
            current_node = current_node["next"]
        return arr

    def insert(self, data, index):
        if index >= self.length:
            return self.append(data)
        
        new_node = {"value": data, "next": None, "prev": None}
        leader = self.traverse(index-1)
        follower = leader["next"]
        leader["next"] = new_node
        new_node["prev"] = leader
        new_node["next"] = follower
        follower["prev"] = new_node
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
        leader = self.traverse(index - 1)
        temp = leader["next"]
        follower= temp["next"]
        leader["next"] = follower
        follower["prev"] = leader       
        self.length -= 1
        return self.printList()



         


x = Doubly_llist()
x.append(6)
x.append(5)
print(x.append(0))
print(x.remove(1),x.length)

