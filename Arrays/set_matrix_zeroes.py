"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/

Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
 

Example 1:
Input: matrix = 
[[1,1,1],
[1,0,1],
[1,1,1]]

Output: 
[[1,0,1],
[0,0,0],
[1,0,1]]

Example 2:
Input: matrix = 
[[0,1,2,0],
[3,4,5,2],
[1,3,1,5]]
Output: 
[[0,0,0,0],
[0,4,5,0],
[0,3,1,0]]
"""


def setZeroes(matrix):
    marked_rows = set()
    marked_columns = set()
    # iterate through matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # if the element is 0
            if matrix[i][j] == 0:
                # mark the row and column so we can set them to zero later
                marked_rows.add(i)
                marked_columns.add(j)
    # iterate through matrix again and set marked rows and columns to 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in marked_rows or j in marked_columns:
                matrix[i][j] = 0
    return matrix


# expected [[1,0,1],[0,0,0],[1,0,1]]
print(setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
