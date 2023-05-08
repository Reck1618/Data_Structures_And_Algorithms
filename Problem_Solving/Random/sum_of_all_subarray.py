"""
Given an integer array array of size n, find sum of all sub-arrays of given array. 

Examples 1: 
Input   : arr[1,2,3] 
Output  : 20

Example 2:
Input  : arr[1,2,3,4] 
Output : 50
"""
# Optimal Solution
def sub_sum_optimal(arr):
    ans = 0
    n = len(arr)
    
    for i in range(0, n):
        ans += (arr[i] * (n - i) * (i + 1))
    return ans



# Normal Solution
def sub_sum(arr):
    ans = 0
    for c in range(1,len(arr) + 1):
        start = 0
        for i in range(len(arr)):

            if i - start + 1 >= c:
                ans += sum(arr[start:i + 1])
                start += 1
    return ans


def main():
    print(sub_sum([1,2,3,4]))
    print(sub_sum_optimal([1,2,3,4]))

main()