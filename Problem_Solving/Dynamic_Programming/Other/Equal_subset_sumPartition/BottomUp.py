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
    
    dp = set()
    dp.add(0)
    for i in range(len(nums)):
        nextdp = set()
        for j in dp:
            if j + nums[i] == target:
                return True
            nextdp.add(j + nums[i])
            nextdp.add(j)
        dp = nextdp
    return False

def main():
  print("Can partition: " + str(can_partition([1, 5, 11, 5])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
