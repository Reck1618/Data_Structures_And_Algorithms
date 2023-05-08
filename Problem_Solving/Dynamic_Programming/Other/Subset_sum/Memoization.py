"""
Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number S.

Example 1:#
Input: {1, 2, 3, 7}, S=6
Output: True

Example 2:#
Input: {1, 2, 7, 1, 5}, S=10
Output: True

Example 3:#
Input: {1, 3, 4, 8}, S=6
Output: False
"""

def can_partition(nums, sum):
    dp = [[False for i in range(sum + 1)] for y in range(len(nums))]
    return solve(dp, nums, sum, 0)

def solve(dp, nums, sum, index):
    n = len(nums)
    
    if sum == 0:
        return True
    if index >= n:
        return False

    if dp[index][sum] != False:
        return dp[index][sum]
    
    if nums[index] <= sum:
        if solve(dp, nums, sum - nums[index], index + 1):
            return True
    dp[index][sum] = solve(dp, nums, sum, index + 1)

    return dp[n-1][sum]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()