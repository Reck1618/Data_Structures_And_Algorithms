"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example-1
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example-2 
Input: String="cbbebi", K=10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".
"""
def longest_substring_with_k_distinct(s, k):
  store = {}
  start = 0
  length = 0

  for i in range(len(s)):
    if s[i] in store:
      store[s[i]] += 1
    else:
      store[s[i]] = 1
    
    while len(store) > k:
      if store[s[start]] == 1:
        del store[s[start]]
      else:
        store[s[start]] -= 1
      start += 1

    length = max(length, (i - start + 1))

  return length

# Time Complexity = O(N)
# Space Complexity = O(N)

def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("nutdrgzdrkrvfdfcvzuunxwlzegjukhkjpvqruitobiahxhgdrpqttsebjsg", 11)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))

main()