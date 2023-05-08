"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
"""
def pair_with_targetsum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
      currentsum = arr[left] + arr[right]

      if currentsum == target:
        return [left, right]
      elif currentsum > target:
        right -= 1
      else:
        left += 1

    return [-1, -1]
    
# Time Complexity : O(N)
# Space Complexity : O(1)

def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
