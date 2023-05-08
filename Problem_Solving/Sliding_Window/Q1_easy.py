"""
Given an array of positive numbers and a positive number k, find the maximum sum of any contiguous subarray of size k.

Example-1
Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example-2
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""
def max_sub_array_of_size_k(k, arr):
  max_sum, cur_sum, start = 0, 0, 0

  for end in range(len(arr)):
    cur_sum += arr[end]

    if end >= k-1:
      max_sum = max(max_sum, cur_sum)
      cur_sum -= arr[start]
      start += 1

  return max_sum

# Time Complexity = O(N)
# Space Complexity = O(1)


def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
