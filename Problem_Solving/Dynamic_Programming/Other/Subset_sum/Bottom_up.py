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
    dp = set()
    dp.add(0)

    for i in range(len(nums)):
        next_dp = set()
        for j in dp:
            if j + nums[i] == sum:
                return True
            next_dp.add(j + nums[i])
            next_dp.add(j)
        dp = next_dp
    return False



def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))

main()

