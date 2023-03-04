# Impliment Bubble Sort.

def bubble_sort(array):
    for i in range(len(array)-1):
        swapped = False
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break
    return array

print(bubble_sort([9,2,3,6,7,2,3,7,1]))