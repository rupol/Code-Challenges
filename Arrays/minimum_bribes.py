"""
https://www.hackerrank.com/challenges/new-year-chaos/problem

It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by 1 from 1 at the front of the line to n at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if n=8 and Person 5 bribes Person 4, the queue will look like this: 1,2,3,5,4,6,7,8.

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!

Function Description

Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.
"""

# input: array of integers, representing the order of people standing in line for a queue
# output: minimum number of swaps that took place to get the queue into its current state
# queue is originally in order from 1 to n
# a person can only swap with the person directly in front of them
# if more than 2 swaps are needed, print "Too chaotic"


def minimumBribes(q):
    # try to get the queue back in order
    number_of_swaps = 0
    # if it takes more than two swaps, the state is invalid
    if number_of_swaps > 2:
        print("Too chaotic")
    return number_of_swaps


print(minimumBribes([1, 2, 3, 5, 4, 6, 7, 8]))
