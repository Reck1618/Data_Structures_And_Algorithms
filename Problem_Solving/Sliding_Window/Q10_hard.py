"""
Given a string and a pattern, find the smallest substring in the 
given string which has all the character occurrences of the given pattern.

Example - 1
Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Example - 2
Input: String="aabdec", Pattern="abac"
Output: "aabdec"
Explanation: The smallest substring having all character occurrences of the pattern is "aabdec"

Example - 3
Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
"""
def find_substring(str1, pattern):
  start, sub_start, min_length = 0, 0, len(str1)
  matched = 0
  store = {}

  for i in pattern:
    if i not in store:
      store[i] = 0
    store[i] += 1

  for i in range(len(str1)):
    if str1[i] in store:
      store[str1[i]] -= 1
      if store[str1[i]] == 0:
        matched += 1

    while matched == len(store):
      if min_length > (i - start + 1):
        min_length = i - start + 1
        sub_start = start 

      if str1[start] in store:
        if store[str1[start]] == 0:
          matched -= 1
        store[str1[start]] += 1

      start += 1

  return str1[sub_start: sub_start + min_length]
  

def main():
  print(find_substring("aabdec", "abc"))
  print(find_substring("aabdec", "abac"))
  print(find_substring("abdbca", "abc"))
  print(find_substring("ADOBECODEBANC", "ABC"))

main()