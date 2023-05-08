"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.
A string's subsequence is a new string formed from the original string by deleting some 
(can be none) of the characters without disturbing the remaining characters' relative positions. 
(i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).The test cases are generated so 
that the answer fits on a 32-bit signed integer.

Example
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
"""

def numDistinct(s,t):
    cache = {}

    def dfs(i, j):
        if j == len(t):
            return 1
        if i == len(s):
            return 0

        if (i,j) in cache:
            return cache[(i,j)]

        if s[i] == t[j]:
            cache[(i,j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
        else:
            cache[(i,j)] = dfs(i + 1, j)
        
        return cache[(i, j)]
    return dfs(0,0)

def main():
    print(numDistinct("rabbbit", "rabbit"))

main()