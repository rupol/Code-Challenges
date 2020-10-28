"""
https://leetcode.com/problems/increasing-triplet-subsequence/

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:
Input: [1,2,3,4,5]
Output: true

Example 2:
Input: [5,4,3,2,1]
Output: false
"""

# works to find increasing subarray (contiguous)
"""
def increasingTriplet(nums):
    # iterate through the array
    for i in range(len(nums) - 2):
        print(nums[i], nums[i+1], nums[i+2])
        # determine if window contains an increasing subsequence
        if nums[i] < nums[i+1] < nums[i+2]:
            return True

    return False
"""


def increasingTriplet(nums):
    # use two thresholds to divide the subsequence
    lower = upper = float('inf')

    # iterate through nums
    for num in nums:
        # if current number is less than the lower threshold
        if num <= lower:
            # set lower threshold to number
            lower = num
        # if current number is less than upper threshold
        elif num <= upper:
            # set upper threshold to number
            upper = num
        # if current number is greater than both thresholds
        else:
            # we have an increasing subsequence
            return True
    return False


print(increasingTriplet([1, 2, 3, 4, 5]))  # expected true
print(increasingTriplet([5, 4, 3, 2, 1]))  # expected false
print(increasingTriplet([2, 1, 5, 0, 4, 6]))  # expected true
