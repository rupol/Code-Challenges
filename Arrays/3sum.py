"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""
# input: array of numbers
# output: all sets of three numbers in the array that add up to 0


def threeSum(nums):
    # sort the array
    nums.sort()
    triplets = []
    # iterate through the array
    for i in range(len(nums)):
        # Imagine we are at index i and we have invoked the 2SUM problem from index i+1 to end of the array. Now once the 2SUM terminates, we will have a list of all triplets which include nums[i]
        # To avoid duplicates, we must skip all nums[i] where nums[i] == nums[i-1]
        if i > 0 and nums[i] == nums[i-1]:
            continue

        target = nums[i]*-1
        start = i+1
        end = len(nums) - 1
        while start < end:
            if nums[start] + nums[end] == target:
                triplets.append([nums[i], nums[start], nums[end]])
                start = start + 1
                while start < end and nums[start] == nums[start - 1]:
                    start = start + 1
            elif nums[start] + nums[end] < target:
                start = start + 1
            else:
                end = end - 1
    return triplets


print(threeSum([-1, 0, 1, 2, -1, -4]))
