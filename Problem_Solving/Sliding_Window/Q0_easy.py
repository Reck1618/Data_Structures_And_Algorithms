"""
Given an array, find the average of all subarrays of K contiguous elements in it.

Example
Input = [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output = [2.2, 2.8, 2.4, 3.6, 2.8]
"""

def find_averages_of_subarrays(K, arr):
    cur_sum, start = 0, 0
    ans = []

    for i in range(len(arr)):
        cur_sum += arr[i]

        if i >= K - 1:
            ans.append(cur_sum/K)
            cur_sum -= arr[start]
            start += 1
    return ans

# Time Complexity = O(N)
# Space Complexity = O(1)

def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()
