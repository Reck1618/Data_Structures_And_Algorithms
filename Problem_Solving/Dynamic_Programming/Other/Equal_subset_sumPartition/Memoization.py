"""
Given a set of positive numbers, find if we can partition it into two
subsets such that the sum of elements in both subsets is equal.

Example 1:
Input: {1, 2, 3, 4}
Output: True
 
Example 2:
Input: {1, 1, 3, 4, 7}
Output: True

Example 3:
Input: {2, 3, 4, 6}
Output: False
"""
def can_partition(nums):
    total = sum(nums)
    target = total // 2
    if total % 2 != 0:
        return False

    dp = [[-1 for i in range(target + 1)] for y in range(len(nums))]
    return solve(dp, nums, target, 0)
     
def solve(dp, nums, target, index):
    n = len(nums)
    if target == 0:
        return True

    if index >= n:
        return False
    
    if dp[index][target] != -1:
        return dp[index][target]

    if nums[index] <= target:
        if solve(dp, nums, target - nums[index], index + 1):
            return True
    dp[index][target] = solve(dp, nums, target, index + 1)

    return dp[n - 1][target]


def main():
  print("Can partition: " + str(can_partition([1, 5, 11, 5])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
