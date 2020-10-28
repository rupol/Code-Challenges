"""
Moving Zeroes

Write a function that takes an array of integers and moves each non-zero integer to the left side of the array, then returns the altered array. The order of the non-zero integers does not matter in the mutated array.

Examples
Sample input: [0, 3, 1, 0, -2]
Expected output: 3
Expected output array state: [3, 1, -2, 0, 0]

Sample input: [4, 2, 1, 5]
Expected output: 4
Expected output array state: [4, 2, 1, 5]
"""
# return the array with all non-zero integers to the left


def moving_zeroes(arr):
    # create a new array
    result = [0] * len(arr)
    count = 0
    # loop through the array
    for num in arr:
        # if num is not 0, insert it at the front of the new array
        if num != 0:
            result[count] = num
            count += 1
    # return sorted array
    return result


print(moving_zeroes([4, 2, 1, 5]))  # expected [4, 2, 1, 5]
print(moving_zeroes([0, 3, 1, 0, -2]))  # expected [3, 1, -2, 0, 0]
