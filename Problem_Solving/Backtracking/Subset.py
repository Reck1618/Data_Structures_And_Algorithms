"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

# Backtracking
def subsets_1(nums):
    result = []

    def backtracking(first = 0, cur_set = []):
        if len(cur_set) == k:
            result.append(cur_set[:])
            return
        
        for i in range(first, len(nums)):
            cur_set.append(nums[i])
            backtracking(i + 1, cur_set)
            cur_set.pop()
        
    for k in range(len(nums) + 1):
        backtracking()

    return result

# DFS
def subsets_2(nums):
    result = []
    cur_set = []

    def dfs(i = 0):
        if i >= len(nums):
            result.append(cur_set[:])
            return
        
        cur_set.append(nums[i])
        dfs(i + 1)

        cur_set.pop()
        dfs(i + 1)

    dfs()
    return result


def main():
    print(subsets_1([1,2,3]))
    print(subsets_1([1]))
    print(subsets_2([1,2,3]))
    print(subsets_2([1]))


main()
