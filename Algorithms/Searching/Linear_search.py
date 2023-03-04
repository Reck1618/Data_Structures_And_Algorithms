# Implement Linear Search. 

def linear_search(array, target):
    length = len(array)
    for i in range(length):
        if array[i] == target:
            return True
    return False

print(linear_search([1,3,4,5,6,7,8,9], 10))