# Implement Selection Sort.

def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
        array[min], array[i] = array[i], array[min]
    return array


print(selection_sort([1,5,2,4,0,5,1]))
        
         