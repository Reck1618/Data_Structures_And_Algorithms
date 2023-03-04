# Implement Quick Sort.

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1

            array[i], array[j] = array[j], array[i]
        

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)
    return array

data = [5,1,9,2,4,8,2,6,0,3,67,44,0,33,66]
print(quick_sort(data , 0, len(data) - 1))