"""
Given an array of positive numbers and a positive number s, 
find the length of the smallest contiguous subarray whose sum 
is greater than or equal to s. Return 0 if no such subarray exists.

Example 
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
"""
def smallest_subarray_sum(s, arr):
  start, curr_sum, length = 0, 0, float('inf')

  for i in range(len(arr)):
    curr_sum += arr[i]

    while curr_sum >= s:
      length = min(length, (i - start + 1))
      curr_sum -= arr[start]
      start += 1
  if length == float('inf'):
    return 0
  return length

# Time Complexity = O(N+N), which is asymptotically equivalent to O(N)
# Space Complexity = O(1)

def main():
  print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))


main()
