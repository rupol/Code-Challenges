'''
Write a function that receives an array of integers and returns an array consisting of the product of all numbers in the array _except_ the number at that index.

For example, given
[1, 7, 3, 4]

your function should return
[84, 12, 28, 21]

by calculating
[7*3*4, 1*3*4, 1*7*4, 1*7*3]

In the above example, the final value at index 0 is the product of every number in the input array _except_ the number at index 0.

Input: a List of integers
Returns: a List of integers
'''

import math
# return an array where each item is the product of all other items


def product_of_all_other_numbers(arr):
    # multiply all items in the array together
    mult_total = math.prod(arr)
    # create an array to save multiplications in
    result = [0] * len(arr)
    # iterate over the original array
    for i, val in enumerate(arr):
        # divide the mult_total by the current value
        # save the resulting number in the correct position of result
        result[i] = mult_total // val
    return result


arr = [1, 7, 3, 4]
print(product_of_all_other_numbers(arr))
print(f'expected: {[7*3*4, 1*3*4, 1*7*4, 1*7*3]}')
