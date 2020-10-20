"""
https://www.hackerrank.com/challenges/array-splitting/
Nikita just came up with a new array game. The rules are as follows:

Initially, Nikita has an array of integers.

In each move, Nikita must partition the array into 2 non-empty contiguous parts such that the sum of the elements in the left partition is equal to the sum of the elements in the right partition. If Nikita can make such a move, she gets 1 point; otherwise, the game ends.

After each successful move, Nikita discards either the left partition or the right partition and continues playing by using the remaining partition as array arr.

Nikita loves this game and wants your help getting the best score possible. Given arr, can you find and print the maximum number of points she can score?

For example, Nikita starts with the array arr=[1,2,3,6]. She first splits it into a1=[1,2,3] and , a2=[6] then discards a2. She then has an array [1,2,3], which she splits into a1=[1,2] and a2=[3]. This cannot be further split, so Nikita scored 2.

Function Description

Complete the arraySplitting function in the editor below. It should return an integer that reperesents the number of times Nikita can split the array.
"""


def splitArray(arr):
    # the sum or array1 must equal the sum of array 2
    # compute the sum of the array
    arr_sum = sum(arr)
    # traverse, keeping track of current sum
    current_sum = 0
    for i in range(0, len(arr)):
        # if current sum = sum / 2, we're at the splitting point
        current_sum += arr[i]
        print(current_sum, arr_sum // 2)
        # if the current sum is odd, we can't split evenly
        if arr_sum % 2 != 0:
            return -1
        if current_sum == arr_sum // 2:
            # split into two arrays at splitting point
            arr1 = arr[:i+1]
            arr2 = arr[i+1:]
            # discard one of the arrays (the shorter array)
            # how to do this optimally?
            if len(arr1) > len(arr2):
                return arr1
            else:
                return arr2
    # if no split possible, return -1
    return -1


def arraySplitting(arr, points=0):
    new_array = splitArray(arr)
    # base case: no more splitting possible
    if new_array == -1:
        return points

    # split the array
    # we've earned a point
    points += 1
    print(new_array)
    points = arraySplitting(new_array, points=points)

    return points


print(arraySplitting([4, 1, 0, 1, 1, 0, 1]))  # expected 3

# print(splitArray([1, 2, 3, 6]))
