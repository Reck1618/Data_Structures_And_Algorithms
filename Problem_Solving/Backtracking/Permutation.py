"""
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
"""

# Top Down
def permutation_1(nums):
    visit = set()
    result = []

    def backtracking(subset = []):
        if len(subset) == len(nums):
            result.append(subset)
            return

        for i in range(len(nums)):
            if i not in visit:
                visit.add(i)
                backtracking(subset + [nums[i]])
                visit.remove(i)

    backtracking()
    return result


# Bottom Up
def permutation_2(nums):
    result = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permutation_2(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    return result



def main():
  print(permutation_1([1,2,3]))
  print(permutation_1([0,1]))
  print(permutation_1([1]))
  print(permutation_2([1,2,3]))
  print(permutation_2([0,1]))
  print(permutation_2([1]))
main()

