"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without 
changing the order of the remaining elements. For example, [3,6,2,7] is a 
subsequence of the array [0,3,1,6,2,2,7].

Example
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""

# Binary Search
import bisect

def length_of_lis_1(nums):
    temp = []
    temp.append(nums[0])

    for i in range(1, len(nums)):
        if nums[i] > temp[-1]:
            temp.append(nums[i])
        else:
            index = bisect.bisect_left(temp, nums[i])
            temp[index] = nums[i]
    
    return len(temp)

# Time Complexity : O(n logn)
# Space Complexity : O(1)

def main_1():
    print(length_of_lis_1([10,9,2,5,3,7,101,18]))
main_1()


# Dynamic Programming
def length_of_lis(nums):
    LIS = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)

# Time Complexity = O(N^2)
# Space Complexity = O(N)
def main():
    print(length_of_lis([10,9,2,5,3,7,101,18]))

main()