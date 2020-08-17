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

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.  
# Example 1:
#
# Input:
# ```
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ] 
# ```
# Output: [1,2,3,6,9,8,7,4,5]  
# Example 2:  
#
# Input:
# ```
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]  
# ```
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]  


# mysolution
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        spiral_list = list()
        rows, cols = 0, -1
        row_direction, col_direction = 0, 1
        row_leg, col_leg = len(matrix[0]), len(matrix) - 1
        leg_count = 0

        for _ in range(len(matrix[0]) * len(matrix)):
            rows += row_direction
            cols += col_direction
            spiral_list.append(matrix[rows][cols])
            leg_count += 1

            # change direction 行
            if (col_direction != 0 and leg_count == row_leg) or (row_direction != 0 and leg_count == col_leg):
                if row_direction:
                    col_leg -= 1
                    row_direction = -row_direction
                elif col_direction:
                    row_leg -= 1
                col_direction, row_direction = row_direction, col_direction
                leg_count = 0
        return spiral_list


# +
import unittest


class LeetcodeTest0054(unittest.TestCase):
    solution = Solution()

    def test_case1(self):
        test_input = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        test_output = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEquals(self.solution.spiralOrder(test_input), test_output)

    def test_case2(self):
        test_input = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        test_output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEquals(self.solution.spiralOrder(test_input), test_output)

    def test_case3(self):
        test_input = []
        test_output = []
        self.assertEquals(self.solution.spiralOrder(test_input), test_output)

    def test_case4(self):
        test_input = [[]]
        test_output = []
        self.assertEquals(self.solution.spiralOrder(test_input), test_output)
        

unittest.main(argv=['ignored', '-v'], exit=False)


# -

# [Jake's solution](https://github.com/jakehoare/leetcode/blob/master/python_1_to_1000/054_Spiral_Matrix.py)  
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.  
# Use row_leg and col_leg to track the max number of moves before turning.
# Decrease row_leg and col_leg then turning.  
# Time - O(m * n)  
# Space - O(1)  

# Jake's solution
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        spiral = []
        row, col = 0, -1
        d_row, d_col = 0, 1     # movement direction
        row_leg, col_leg = len(matrix[0]), len(
            matrix)-1    # steps before change of direction
        # count of steps in current direction
        leg_count = 0

        for _ in range(len(matrix[0]) * len(matrix)):

            row += d_row
            col += d_col
            spiral.append(matrix[row][col])
            leg_count += 1

            # change direction
            if (d_col != 0 and leg_count == row_leg) or (d_row != 0 and leg_count == col_leg):
                if d_col != 0:
                    row_leg -= 1
                else:
                    col_leg -= 1
                d_row, d_col = d_col, -d_row
                leg_count = 0

        return spiral