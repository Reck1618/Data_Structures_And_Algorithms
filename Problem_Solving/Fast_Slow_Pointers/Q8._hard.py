"""
We are given an array containing positive and negative numbers. Suppose the array 
contains a number M at a particular index. Now, if M is positive we will move 
forward M indices and if M is negative move backwards M indices. You should assume 
that the array is circular which means two things:

If, while moving forward, we reach the end of the array, we will jump to the first 
element to continue the movement. If, while moving backward, we reach the beginning 
of the array, we will jump to the last element to continue the movement. Write a 
method to determine if the array has a cycle. The cycle should have more than one 
element and should follow one direction which means the cycle should not contain 
both forward and backward movements.

Example 1:
Input: [1, 2, -1, 2, 2]
Output: true
Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0

Example 2:
Input: [2, 2, -1, 2]
Output: true
Explanation: The array has a cycle among indices: 1 -> 3 -> 1

Example 3:
Input: [2, 1, -1, -2]
Output: false
Explanation: The array does not have any cycle.
"""

def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        is_forward = arr[i] >= 0
        slow, fast = i, i

        while True:
            slow = find_next_index(arr, is_forward, slow)

            fast = find_next_index(arr, is_forward, fast)
            if fast != -1:
                fast = find_next_index(arr, is_forward, fast)
            
            if slow == -1 or fast == -1 or slow == fast:
                break
        
        if slow != -1 and slow == fast:
            return True
    return False

def find_next_index(arr, is_forward, cur_index):
    direction = arr[cur_index] >= 0

    if is_forward != direction:
        return -1

    next_index = (cur_index + arr[cur_index]) % len(arr)

    if next_index == cur_index:
        next_index = -1
    return next_index

# Time Complexity : O(N^2)
# Space Complexity : O(1)

def main():
  print(circular_array_loop_exists([1, 2, -1, 2, 2]))
  print(circular_array_loop_exists([2, 2, -1, 2]))
  print(circular_array_loop_exists([2, 1, -1, -2]))


main()
