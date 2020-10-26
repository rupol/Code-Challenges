"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""
# input: array of strings
# output: array of arrays; each internal array should contain a group of anagrams found in the original array (rearranged letters that also forms a word)


def groupAnagrams(strs):
    # create a dict of "sorted words"
    # key: sorted word
    # value: array of anagrams
    sorted_words = dict()

    # for each word in strs
    for word in strs:
        sorted_word = (''.join(sorted(word)))
        # add sorted_word: word if not in dict
        if sorted_word not in sorted_words:
            sorted_words[sorted_word] = [word]
        # otherwise, append word to dict[sorted_word]
        else:
            sorted_words[sorted_word].append(word)

    result = list(map(list, (sorted_words.values())))
    return result


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
