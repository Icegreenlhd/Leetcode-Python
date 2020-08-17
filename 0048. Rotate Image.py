# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # my solution 1, zip
# - Time:$O(n^2)$
# - Space:$O(n)$

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [list(i)[::-1] for i in zip(*matrix)]
#         matrix[:] = list(map(list, zip(*matrix[::-1])))
        return


# # my solution2, by index
# - Time: $O(n^2)$
# - Space: $O(1)$

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
                
        for i in range(len(matrix)):
            for j in range(len(matrix[0])//2):
                matrix[i][j], matrix[i][len(matrix[0])-1-j] = matrix[i][len(matrix[0])-1-j],matrix[i][j]
        return


# 优化
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
                
        for i in range(n):
            matrix[i].reverse()
        return


# # Jake's solution
# Number of layer to rotate is n//2.  For each item along the top side of each layer, save as temp and
# move in the item from the next side, repeating until temp is put into the last side.
# Alternatively - matrix[:] = list(map(list, zip(*matrix[::-1]))).  Reverse the order of row, unpack,
# zip and convert back to lists.
# - Time - O(n^2)
# - Space - O(1)

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        layers = n//2

        for layer in range(layers):
            for i in range(layer, n - layer - 1):
                temp = matrix[layer][i]
                matrix[layer][i] = matrix[n - 1 - i][layer]
                matrix[n - 1 - i][layer] = matrix[n - 1 - layer][n - 1- i]
                matrix[n - 1 - layer][n - 1 - i] = matrix[i][n - 1 - layer]
                matrix[i][n - 1 - layer] = temp


# +
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

matrix[::-1]
