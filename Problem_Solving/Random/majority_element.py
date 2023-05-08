"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
def majority_element(arr):
    store = {}

    for i in arr:
        if i not in store:
            store[i] = 0
        store[i] += 1

        if store[i] > len(arr) // 2:
            return i

def main():
    print(majority_element([2,2,1,1,1,2,2]))

main()