'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


# return the integer that only shows up once in the array
def single_number(arr):
    result = arr[0]

    # do XOR of all elements
    for i in range(1, len(arr)):
        result = result ^ arr[i]
    return result

# XOR (zor) operator: compares two bits
# if identical: 0
# if different: 1


'''
# first pass solution
def single_number(arr):
    # order the array
    arr.sort()
    # loop through the array
    i = 0
    while i < (len(arr)):
        # if i + 1 is the same integer as i, move on
        # if there is no i + 1, you are at the end of the list and that number is the odd one out
        if i == len(arr) - 1:
            return arr[i]
        # if i + 1 is different from i, return that number
        if arr[i] != arr[i + 1]:
            return arr[i]
        # after each pair, i ++ (skip)
        i += 2
'''

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 3, 0, 4, 5, 5, 3, 9, 9, 0, 1]

    print(f"The odd-number-out is {single_number(arr)}")
