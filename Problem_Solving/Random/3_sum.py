"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
Such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
"""

def threeSum(nums):
    nums.sort()
    ans = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            cur_sum = nums[i] + nums[l] + nums[r]
            
            if cur_sum == 0:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            
            elif cur_sum > 0:
                r -= 1
            else:
                l += 1
    return ans

print(threeSum([-1,0,1,2,-1,-4]))