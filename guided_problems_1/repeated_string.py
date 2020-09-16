"""
https://www.hackerrank.com/challenges/repeated-string/problem

Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string.

For example, if the string s='abcac' and n=10, the substring we consider is abcacabcac, the first 10 characters of her infinite string. There are 4 occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Input Format

The first line contains a single string, s.
The second line contains an integer, n.


Output Format

Print a single integer denoting the number of letter a's in the first  letters of the infinite string created by repeating  infinitely many times.

Sample Input
aba
10

Sample Output
7

Explanation
The first n=10 letters of the infinite string are abaabaabaa. Because there are 7 a's, we print 7 on a new line.
"""

# brute force solution


def repeatedStringBrute(s, n):
    substring = ""
    while len(substring) < n:
        substring += s
    # chop off the extra letters on substring so it's n characters long
    substring = substring[0:n]
    print(len(substring), substring)

    num_as = 0
    for char in substring:
        if char == "a":
            num_as += 1

    return num_as


# improved solution
def repeatedString(s, n):
    # I know how many times 'a' appears in s
    num_as_in_s = 0
    for char in s:
        if char == 'a':
            num_as_in_s += 1

    # I know the length of s, so I can figure out how many times s is repeated in the substring
    full_repetitions_of_s = n // len(s)
    # multiply the number of times s is repeated * the number of times 'a' appears in s
    # I need to handle the remainder that's left over
    remainder_length = n % len(s)
    num_as_in_remainder = 0
    remainder_string = s[0:remainder_length]
    for char in remainder_string:
        if char == 'a':
            num_as_in_remainder += 1
    num_as_in_substring = full_repetitions_of_s * num_as_in_s + num_as_in_remainder

    return num_as_in_substring


print(repeatedString("aba", 10))
