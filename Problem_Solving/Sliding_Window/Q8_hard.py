"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.
Permutation is defined as the re-arranging of the characters of the string. 
For example, “abc” has the following six permutations:
abc
acb
bac
bca
cab
cba
If a string has n distinct characters, it will have n! permutations.

Example
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
"""
def find_permutation(str1, pattern):
    start, matched = 0, 0
    store = {}
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
            return True

        if i >= len(pattern) - 1:
            left = str1[start]
            start += 1
            if left in store:
                if store[left] == 0:
                    matched -= 1
                store[left] += 1
    return False

# Time Complexity = O(N)
# Space Complexity = O(N)


def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("abcdeabcdx", "abcdxabcde")))


main()
