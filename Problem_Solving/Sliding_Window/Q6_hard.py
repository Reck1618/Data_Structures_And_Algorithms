"""
Given a string with lowercase letters only, if you are allowed to replace d
no more than k letters with any letter, find the length of the longest substring 
having the same letters after replacement.

Example-1
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".

Example-2
Input: String="deabcc", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""
import unittest
def length_of_longest_substring(s, k):
    start, length, max_frequency = 0, 0, 0
    store = {}

    for i in range(len(s)):
        if s[i] in store:
            store[s[i]] += 1
        else:
            store[s[i]] = 1
        
        max_frequency = max(max_frequency, store[s[i]])

        if (i - start + 1) - max_frequency > k:
            store[s[start]] -= 1
            start += 1
        
        length = max(length, i - start + 1)
    
    return length

# Time Complexity = O(N)
# Space Complexity = O(1)

def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))


main()