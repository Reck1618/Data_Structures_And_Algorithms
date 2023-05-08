"""
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

Example 1:
Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

Example 2:
Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
             [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
"""
def two_pointer(arr, target):
    arr.sort()
    count = 0
    i = 0
    while i < len(arr) - 2:
        left = i + 1
        right = len(arr) - 1

        while left < right:
            cur_sum = arr[i] + arr[left] + arr[right]

            if cur_sum < target:
                count += right - left
                left += 1
            else:
                right -= 1
        
        i += 1
    return count

# Time Complexity : O(N^2)
# Space Complexity : O(N)


def main():
    print(two_pointer([-1, 0, 2, 3], 3))
    print(two_pointer([-1, 4, 2, 1, 3], 5))

main()


# Addition
"""
Write a function to return the list of all such triplets instead of the count. 
How will the time complexity change in this case?
"""
def addition(arr, target):
    arr.sort()
    triplets = []
    for i in range(len(arr) - 2):
        search_pair(arr, target - arr[i], i, triplets)
    return triplets

def search_pair(arr, target_sum, index, triplets):
    left = index + 1
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] < target_sum:

            for i in range(right, left, -1): 
                triplets.append([arr[index], arr[left], arr[i]])
            left += 1
        else:
            right -= 1
    
def main_2():
    print(addition([-1, 0, 2, 3], 3))

main_2()