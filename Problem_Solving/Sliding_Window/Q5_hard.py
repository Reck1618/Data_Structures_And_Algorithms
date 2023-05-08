"""
Given a string, find the length of the longest substring, which has all distinct characters.

Example
Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".
"""

# Solution - 1
def non_repeat_substring_1(str):
    left, length, char_set = 0, 0, set()
    for right in range(len(str)):
        while str[right] in char_set:
            char_set.remove(str[left])
            left += 1

        char_set.add(str[right])
        length = max(length, right - left + 1)
    return length

# Solution - 2
def non_repeat_substring_2(str):
    left, length, char_map = 0, 0, {}
    for right in range(len(str)):
        if str[right] in char_map:
            left = max(left, char_map[str[right]] + 1)
        char_map[str[right]] = right
        length = max(length, right - left + 1)
    return length

# Time Complexity = O(N)
# Space Complexity = O(1) There are only 26 alphabets.

def main():
  print("Length of the longest substring: " + str(non_repeat_substring_1("abcdcabbb")))
  print("Length of the longest substring: " + str(non_repeat_substring_1("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring_2("abccde")))
  print("Length of the longest substring: " + str(non_repeat_substring_2("pwwkew")))


main()