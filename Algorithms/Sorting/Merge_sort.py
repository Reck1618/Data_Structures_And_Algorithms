# Implement Merge Sort. 

def merge_sort(array):
    if len(array) == 1:
        return array

    center = len(array) // 2

    left = array[:center]
    right = array[center:]

    return merge(merge_sort(left),merge_sort(right))

def merge(left,right):
    ans = []
    l = 0
    r = 0

    while l < len(left) and r < len(right):

        if left[l] <= right[r]:
            ans.append(left[l])
            l += 1
        else:
            ans.append(right[r])
            r += 1

    return ans + left[l:] + right[r:]

print(merge_sort([1,2,6,3,5,7,5,1,2,56,2,34,5]))