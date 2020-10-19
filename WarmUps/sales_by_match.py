"""
Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are n=7 socks with colors ar=[1,2,1,2,1,3,2]. There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock

Input Format
The first line contains an integer n, the number of socks represented in ar.
The second line contains  space-separated integers describing the colors ar[i] of the socks in the pile.

Output Format
Return the total number of matching pairs of socks that Alex can sell.

Sample Input
9
10 20 20 10 10 30 50 10 20

Sample Output
3

Explanation
Alex can match three pairs of socks.
"""


def sockMerchant(n, ar):
    number_of_pairs = 0
    # create dictionary
    # key: sock "color"
    # value: number of socks of that "color"
    sock_dict = {}
    for sock in ar:
        if sock not in sock_dict:
            sock_dict[sock] = 1
        else:
            sock_dict[sock] += 1
    # find number of pairs in sock dict
    # divide number of socks for each "color" by 2 (rounding down)
    # add that number to the number of pairs
    for number_of_each_color in sock_dict.values():
        number_of_pairs += number_of_each_color // 2
    return number_of_pairs


print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
