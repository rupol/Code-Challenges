"""
Given an array of integers, there is a sliding window of size `k` which is moving from the left side of the array to the right, one element at a time. You can only interact with the `k` numbers in the window. Return an array consisting of the maximum value of each window of elements.

Example
Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Expected Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""
# return an array with the max value of each window (i to i + k)


def sliding_window_max_queue(nums, k):
    # create a queue that stores useful elements
    # useful element - number in current window that is larger than all numbers to the left
    # insert the first k elements
    # for each element we add
    # get rid of all smaller numbers in the queue

    # add the number to the end of the queue
    # process the remaining elements in nums

    # from k to n - 1
    # the element at the front of the queue is the largest number of current window
    # save that number into output
    pass


# first pass solution
# runtime - O(n * k)
def sliding_window_max(nums, k):
    # create an array to save the max values in
    result = [0] * (len(nums) - (k - 1))
    # iterate through the array
    for i in range(len(nums)):
        # if i is k items from the end of the array
        if i + k <= len(nums):
            # slice out a window from i to i + k
            window = nums[i:i+k]
            # find the max of that subarray
            result[i] = max(window)
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
