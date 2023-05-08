"""
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; 
after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

Example
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
"""
def remove_duplicates(arr):
  left = 1
  
  for right in range(1, len(arr)):
    if arr[right] != arr[right - 1]:
      arr[left] = arr[right]
      left += 1

  return left

# Time Complexity : O(N)
# Space Complexity : O(1)

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()

