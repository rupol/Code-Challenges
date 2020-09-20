"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""
# input: string
# output: longest palindrome found in the string
# even a single letter is a palindrome
# we might want a helper function to tell if a substring is a palindrome or not
# implementation for helper function is to reverse and compare
# we need a variable to hold the current longest substring
# brute force approach: split string into all substrings and test those with the helper function?


palindrome_cache = {}


def is_palindrome(s):
    if s in palindrome_cache:
        return palindrome_cache[s]
    if len(s) <= 1:
        return True
    # if the first and last char match and the inner bit is a palindrome
    result = (s[0] == s[-1] and is_palindrome(s[1:-1]))
    palindrome_cache[s] = result
    return result


def longestPalindrome(s):
    if len(s) == 1:
        return s

    longest_palindrome = ''
    # start with substring of len(s)
    for substring_length in range(len(s), -1, -1):
        # start with first character
        for i in range(len(s) - substring_length + 1):
            substring = s[i: i+substring_length]
            # check if they're a palindrome
            if is_palindrome(substring):
                if len(substring) > len(longest_palindrome):
                    return substring
    return longest_palindrome


a = 'abbe'
print(longestPalindrome(a))  # expected "bb"
