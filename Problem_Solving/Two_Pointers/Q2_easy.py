"""
Given an unsorted array of numbers and a target key, 
remove all instances of key in-place and return the new length of the array.

Example
Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
"""

def remove_element(arr, key):
  left = 0

  for right in range(len(arr)):
    if arr[right] != key:
      arr[left] = arr[right]
      left += 1
  return left

# Time Complexity : O(N)
# Space Complexity : O(1)

def main():
  print("Array new length: " +
        str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
  print("Array new length: " +
        str(remove_element([2, 11, 2, 2, 1], 2)))


main()