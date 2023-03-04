# Implement a Hash Table in python.
# Build methods such as put, get, remove, and hash.

class Hash_table():
    
    def __init__(self):
        self.bucket = 16
        self.hashmap =[ [] for i in range(self.bucket)]

    def __str__(self):                    # Represents the class object as a string
        return str(self.__dict__)

    def hash(self, key):                  # Hash Function
        return len(key) % self.bucket

    def get(self, key):
        hash_value = self.hash(key)
        ref = self.hashmap[hash_value]
        for i in range(len(ref)):
            if ref[i][0] == key:
                return ref[i][1]
        return -1

    def put(self, key, value):
        hash_value = self.hash(key)
        ref = self.hashmap[hash_value]
        for i in range(len(ref)):
            if ref[i][0] == key:
                ref[i][1] = value
                return None
        ref.append([key,value])
        return None

    def remove(self, key):
        hash_value = self.hash(key)
        ref = self.hashmap[hash_value]
        for i in range(len(ref)):
            if ref[i][0] == key:
                ref.pop(i)
                return None
        return None

    def keys(self):                                      # Returns the keys
        keys_array = []
        for i in range(len(self.hashmap)):
            if len(self.hashmap[i]):
                keys_array.append(self.hashmap[i][0][0])
        return keys_array

n = Hash_table()
n.put("name", "ritik")
n.put("age", "22")
n.put("power", "super strength")
n.put("rank", "1")
print(n.get("name"))
n.remove("rank")
print(n.keys())


