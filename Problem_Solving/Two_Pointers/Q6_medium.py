"""
Given an array with positive numbers and a positive target number, find all of its 
contiguous subarrays whose product is less than the target number.

Example 1:
Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

Example 2:
Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.
"""

# Approach 1
def two_pointers(arr, target):
    result = []
    product = 1
    left = 0

    for right in range(len(arr)):
        product *= arr[right]

        while product >= target and left <= right:
            product /= arr[left]
            left += 1

        temp = []
        for i in range(right, left - 1, -1):
            temp.append(arr[i])
            result.append(temp[:])
    return result

def main_2():
    print(two_pointers([2,5,3,10], 30))
main_2()

# Time Complexity : O(N^3)
# Space Complexity : O(N)

    
# Approach 2
def sliding_window(arr, target):
    ans = []
    count = 1

    while count <= len(arr):
        start  = 0
        for i in range(len(arr)):
            if i - start + 1 >= count:
                if pro(arr[start: i + 1]) < target:
                    ans.append(arr[start: i + 1])
                start += 1
        count += 1
    return ans

def pro(arr):
    p = 1
    for i in arr:
        p *= i
    return p 

def main_1():
    print(sliding_window([2, 5, 3, 10], 30))
main_1()


