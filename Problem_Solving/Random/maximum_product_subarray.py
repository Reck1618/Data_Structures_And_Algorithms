"""
Given an integer array nums, find a contiguous non-empty subarray within 
the array that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6

Example 2:
Input: nums = [-2,0,-1]
Output: 0
"""
def maxProduct(nums):
    res = max(nums)
    curMax, curMin = 1, 1

    for n in nums:
        tmp = n * curMax

        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res

def main():
    print(maxProduct([2,3,-2,4]))
    print(maxProduct([-2,0,-1]))
main()
        