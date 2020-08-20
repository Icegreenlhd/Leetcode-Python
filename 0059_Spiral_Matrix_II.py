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

# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.  
#
# Example:  
#
# Input: 3  
# Output:
# ```shell
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]  
# ```


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        row_index, col_index = 0, -1
        row_leg, col_leg = n-1, n
        row_direction, col_direction = 0, 1
        count = 0
        for i in range(1, n ** 2 + 1):
            row_index += row_direction
            col_index += col_direction
            matrix[row_index][col_index] = i
            count += 1

            if (count == row_leg and row_direction != 0) or (count == col_leg and col_direction != 0):
                if col_direction:
                    col_leg -= 1
                else:
                    row_leg -= 1
                    row_direction = -row_direction
                col_direction, row_direction = row_direction, col_direction
                count = 0
        return matrix


# +
import unittest


class LeetcodeTest0059(unittest.TestCase):
    solution = Solution()

    def test_case1(self):
        test_input = 3
        test_output = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
        self.assertEqual(self.solution.generateMatrix(test_input), test_output)

    def test_case2(self):
        test_input = 2
        test_output = [
            [1, 2],
            [4, 3]
        ]
        self.assertEqual(self.solution.generateMatrix(test_input), test_output)

    def test_case3(self):
        test_input = 1
        test_output = [
            [1]
        ]
        self.assertEqual(self.solution.generateMatrix(test_input), test_output)

    def test_case4(self):
        test_input = 0
        test_output = [
        ]
        self.assertEqual(self.solution.generateMatrix(test_input), test_output)


unittest.main(argv=['ignored', '-v'], exit=False)
