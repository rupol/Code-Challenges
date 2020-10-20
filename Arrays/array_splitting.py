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
