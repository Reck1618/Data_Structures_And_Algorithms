"""
Given an array nums of distinct integers, return all the possible subsets. 
You can return the answer in any order.

Example-1 
Input: nums = [1,2,3]
Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], 
        [3, 2], [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""

# Top Down
def permutation_1(nums):
    visit = set()
    result = []

    def backtreacking(subset = []):
        if len(subset) == k:
            result.append(subset)
            return
            
        for i in range(len(nums)):
            if i not in visit:
                visit.add(i)
                backtreacking(subset + [nums[i]])
                visit.remove(i)
        
    for k in range(len(nums) + 1):
        backtreacking()

    return result


def main():
  print(permutation_1([1,2,3]))
  print(permutation_1([0,1]))
  print(permutation_1([1]))

main()

