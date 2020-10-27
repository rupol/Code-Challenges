"""
https://www.hackerrank.com/challenges/plus-minus/problem

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

Example

There are n=5 elements, two positive, two negative and one zero. Their ratios are 0.4, 0.4 and 0.2. Results are printed as:

0.400000
0.400000
0.200000

"""


def plusMinus(arr):
    # iterate through array
    # create count of positive, negative, and zero integers
    positive, negative, zero = 0, 0, 0
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
    total = len(arr)
    positive_proportion = positive/total
    negative_proportion = negative/total
    zero_proportion = zero/total
    print('%.6f' % positive_proportion)
    print('%.6f' % negative_proportion)
    print('%.6f' % zero_proportion)


arr = [1, 1, 0, -1, -1]
print(plusMinus(arr))
