"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

def topK(nums,k):
    visited = {}
    freq = [[] for i in range(len(nums) + 1)]

    for i in range(len(nums)):
        if nums[i] not in visited:
            visited[nums[i]] = 0
        visited[nums[i]] += 1
    
    for i,v in visited.items():
        freq[v].append(i)
    
    ans = []
    for i in range(len(freq) - 1, -1, -1):
        for n in freq[i]:
            ans.append(n)
            if len(ans) == k:
                return ans

print(topK([1,1,1,2,2,3], 2))