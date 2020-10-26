"""

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
"""


# create a set of "seen" characters
# once we reach a character that is already in seen, our substring ends
# keep track of our longest substring length
# replace longest_substring_length only if current is longer
def lengthOfLongestSubstring(s):
    longest_substring_length = 0
    seen = dict()
    start = 0
    # iterate through the string, using a sliding window from 0 to the current character
    for end, character in enumerate(s):
        # if we haven't run into any duplicates yet
        if character not in seen or seen[character] < start:
            # replace longest_substring_length only if current is longer
            longest_substring_length = max(
                longest_substring_length, end-start + 1)
        # if we reach a character that's already been seen
        else:
            # move our window
            start = seen[character] + 1
        seen[character] = end
    return longest_substring_length


print(lengthOfLongestSubstring("abcabcbb"))  # expected 3
