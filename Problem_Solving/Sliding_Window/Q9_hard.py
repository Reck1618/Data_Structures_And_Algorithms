"""
Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to 
repeat characters while finding permutations of a string, we get N! 
permutations (or anagrams) of a string having N
characters. For example, here are the six anagrams of the string “abc”:
abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
"""
def find_string_anagrams(str1, pattern):
  store, result_index = {}, []
  start, matched = 0, 0

  for i in pattern:
    if i not in store:
      store[i] = 0
    store[i] += 1
 

  for i in range(len(str1)):
    right = str1[i]
    if right in store:
      store[right] -= 1
      if store[right] == 0:
        matched += 1

    if matched == len(store):
      result_index.append(start)

    if i >= len(pattern) - 1:
      left = str1[start]
      start += 1
      if left in store:
        if store[left] == 0:
          matched -= 1
        store[left] += 1

  
  return result_indexes

# Time Complexity: O(N)
# Space Complexity: O(N)

def main():
  print(find_string_anagrams("ppqp", "pq"))
  print(find_string_anagrams("abbcabc", "abc"))


main()
