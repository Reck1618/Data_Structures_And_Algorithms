"""
Given an array containing 0s and 1s, if you are allowed to replace no more than k 0s with 1s, 
find the length of the longest contiguous subarray having all 1s.

Example
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
"""
def length_of_longest_substring(arr, k):
    start, length, freq = 0, 0, 0
    for i in range(len(arr)):
        if arr[i] == 1:
            freq += 1
        
        if (i - start + 1) - freq > k:
            if arr[start] == 1:
                freq -= 1
            start += 1
        
        length = max(length, i - start + 1)
    return length


# Time Complexity = O(N)
# Space Complexity = O(1)

def main():
  print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(length_of_longest_substring(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()