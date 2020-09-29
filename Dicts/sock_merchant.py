"""
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are n=7 socks with colors ar=[1,2,1,2,1,3,2]. There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

Function Description
Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock

Input Format
The first line contains an integer n, the number of socks represented in .
The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.

Output Format
Return the total number of matching pairs of socks that John can sell.
"""


def sockMerchant(n, ar):
    sock_count = set()
    # we need to return total count
    # increment a counter every time we make a pair
    num_pairs = 0
    # loop
    for sock_color in ar:
        # if i is in hashtable, then + 1 to pairs and remove key from hashtable
        if sock_color in sock_count:
            num_pairs += 1
            sock_count.remove(sock_color)
        # if i is not in hashtable, add it
        else:
            sock_count.add(sock_color)
    return num_pairs


print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))  # expected: 3
