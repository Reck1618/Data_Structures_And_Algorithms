# Implement Insertion Sort.

# Shifting elements
def insertion_sort(array):
    for i in range(len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = key

    return array

print(insertion_sort([9,2,3,6,7,2,3,7,1]))

# Swaaping elements
def insertion_sort_1(array):
    for i in range(len(array)):
        key = i
        j = i - 1
        while j >= 0 and array[key] < array[j]:
            array[j], array[key] = array[key], array[j]
            key -= 1
            j -= 1

    return array
print(insertion_sort_1([9,2,3,6,7,2,3,7,1]))