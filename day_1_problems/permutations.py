from itertools import permutations
# input: array of unique integers
# output: array of all permutations of those integers
# no particular order
# empty array should return an empty array


def arrPermutations(arr):
    return [list(perm) for perm in list(permutations(arr))]


array = [1, 2, 3]
print(arrPermutations(array))
