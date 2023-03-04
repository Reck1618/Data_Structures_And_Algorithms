# Implement Binary Search.

def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low < high:
        mid = low + (high - low) // 2 

        if array[mid] == target:
            return True
        
        elif target < array[mid]:
            high = mid - 1

        elif target > array[mid]:
            low = mid + 1

    return False 


print(binary_search([i for i in range(10)], 2))
