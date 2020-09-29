# input: an array of integers, length n
# output: sum of array elements

def aVeryBigSum(ar):
    sum = 0
    for num in ar:
        sum += num
    return sum


array = [1000000001, 1000000002,
         1000000003, 1000000004, 1000000005]
print(aVeryBigSum(array))


# input: square matrix
# e.g.  1 2 3
#       4 5 6
#       9 8 9
# output: absolute difference between the sums of matrix diagonals
# e.g. 1 + 5 + 9 = 15; 3 + 5 + 9 = 17; |15 - 17| = 2
def diagonalDifference(arr):
    return arr


arr = [[11, 2, 4],
       [4, 5, 6],
       [10, 8, -12]]
# 11 + 5 + (-12) = 4
# 4 + 5 + 10 = 19
# |4 - 19| = 15
print(diagonalDifference(arr))  # expected: 15
