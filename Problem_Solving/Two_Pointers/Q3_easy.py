"""
Given a sorted array, create a new array containing squares 
of all the numbers of the input array in the sorted order.

Example
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
"""

def make_squares(arr):
  squares = [0 for i in range(len(arr))]
  left, right = 0, len(arr) - 1
  n = len(arr) - 1

  while left <= right:
    l = arr[left] ** 2
    r = arr[right] ** 2
    if l > r:
      squares[n] = l
      left += 1
    else:
      squares[n] = r
      right -= 1

    n -= 1
    
  return squares

# Time Complexity : O(N)
# Space Complexity : O(N)

def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
