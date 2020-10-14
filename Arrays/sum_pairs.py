""""
Find all the pairs of two integers in an unsorted array that sum up to a given S. For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.
"""
# input: array, sum (s)
# output: return an array with the pairs in array that add up to s


def sum_pairs(array, s):
    # dict
    # key: item
    # value: sum - item
    sum_dictionary = {}
    for item in array:
        sum_dictionary[s - item] = item

    print(sum_dictionary)
    result_array = []

    # loop through dict
    for item in array:
        # search to see if the item exists as a value in my dict
        if item in sum_dictionary:
            # if it does, I've found a pair
            # add it to a result array
            result_array.append([sum_dictionary[item], item])

    return result_array


array = [3, 5, 2, -4, 8, 11]
s = 7

print(sum_pairs(array, s))
