# Implement a stack, built with array. 
# Add methods such as peek, push, and pop.

class Stack():
    
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        if len(self.array) == 0:
            return None
        return self.array[len(self.array) - 1]


    def push(self, data):
        self.array.append(data)

    def pop(self):
        pop_item = self.array[len(self.array) - 1]
        del self.array[len(self.array) - 1]
        return pop_item

    
x = Stack()
print(x.peek())
x.push("google")
x.push("hello")
x.push("microsoft")
print(x.pop())
print(x.peek())
print(x.array)
