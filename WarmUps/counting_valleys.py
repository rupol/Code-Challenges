"""
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps steps, for every step it was noted if it was an uphill, U, or a downhill, D step. Hikes always start and end at sea level, and each step up or down represents a 1 unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.

A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Example

steps = [DDUUUUDD]

The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain 2 units high. Finally, the hiker returns to sea level and ends the hike.

Function Description

Complete the countingValleys function in the editor below.

countingValleys has the following parameter(s):

int steps: the number of steps on the hike
string path: a string describing the path

Returns
int: the number of valleys traversed

Input Format
The first line contains an integer steps, the number of steps in the hike.
The second line contains a single string path, of  characters that describe the path.

Sample Input
8
UDDDUDUU

Sample Output
1
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# input: number of steps, path array, where each element represents a step up (U) or down (D) from sea level
# output: the number of valleys walked
# a valley is defined as a sequence of consecutive steps below sea level


def countingValleys(steps, path):
    # keep track of elevation (so we know when we enter/exit a valley)
    elevation = 0
    # keep track of number of valleys walked
    num_valleys = 0
    # iterate through path, incrementing elevation up and down
    for step in path:
        # increment num_valleys if elevation is 0 and we're stepping down (entering a valley)
        if elevation == 0 and step == "D":
            num_valleys += 1
        # move elevation up or down depending on direction stepped
        if step == "U":
            elevation += 1
        elif step == "D":
            elevation -= 1

    return num_valleys


path_a = "DDUUDDUDUUUD"
print(countingValleys(12, path_a))
