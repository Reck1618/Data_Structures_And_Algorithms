"""
Given a string and a list of words, find all the starting indices of substrings in the given string 
that are a concatenation of all the given words exactly once without any overlapping of words. 
It is given that all words are of the same length.

Example 1:
Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

Example 2:
Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
"""
def test(str1, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result = []
    words_count = len(words)
    word_length = len(words[0])

    for i in range((len(str1) - words_count * word_length) + 1):
        words_seen = {}
        for j in range(0, words_count):
            next_word = i + j * word_length
            word = str1[next_word: next_word + word_length]

            if word not in word_frequency:
                break

            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            if words_seen[word] > word_frequency.get(word, 0):
                break

            if j + 1 == words_count:
                result.append(i)

    return result






def main():
    print(test("catfoxcat", ["cat", "fox"]))
    print(test("catcatfoxfox", ["cat", "fox"]))

main()