from itertools import permutations
# input: array of unique integers
# output: array of all permutations of those integers
# no particular order
# empty array should return an empty array


def permutations1(arr):
    return [list(perm) for perm in list(permutations(arr))]


def permHelper(arr, perm, perms):
    # if arr is empty, add permutation to end of permutations list
    # otherwise, iterate through array
    # create a new array with all numbers except current num
    pass


def permutations2(arr):
    return arr


array = [1, 2, 3]
print(permutations1(array))
print(permutations2(array))
