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

# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# 1. Each row must contain the digits `1-9` without repetition.
# 2. Each column must contain the digits `1-9` without repetition.
# 3. Each of the 9 `3x3` sub-boxes of the grid must contain the digits `1-9` without repetition.
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" width=30%>
#
# The Sudoku board could be partially filled, where empty cells are filled with the character `'.'`.
#
# Example 1:
# ```
# Input:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
# ```
# Example 2:
# ```
# Input:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being 
#     modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
# ```
# Note:
#
# - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# - Only the filled cells need to be validated according to the mentioned rules.
# - The given board contain only digits 1-9 and the character '.'.
# - The given board size is always 9x9.

# # my solution 1, simple 

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = [[]for _ in range(9)]
        rows = [[]for _ in range(9)]
        bors = [[]for _ in range(9)]

        for i in range(9):
            for j in range(9):
                sym = board[i][j]
                if sym != ".":
                    if sym not in cols[i] and sym not in rows[j] and sym not in bors[i//3*3+j//3]:
                        cols[i].append(sym)
                        rows[j].append(sym)
                        bors[i//3*3+j//3].append(sym)
                    else:
                        return False
        return True


# modified details
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = [[]for _ in range(9)]
        rows = [[]for _ in range(9)]
        bors = [[]for _ in range(9)]

        for i in range(9):
            for j in range(9):
                sym = board[i][j]
                if sym != ".":
                    if sym in cols[i] and sym in rows[j] and sym in bors[i//3*3+j//3]:
                        return False
                    cols[i].append(sym)
                    rows[j].append(sym)
                    bors[i//3*3+j//3].append(sym)
                        
        return True


# # Jake's solution
# Create a set of digits seen in each row, column and box.  False if any duplicates.
# - Time - O(n^2) for board of side n
# - Space - O(n)

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        size = 9
        digits = {str(i) for i in range(1,10)}
        rows = [set() for _ in range(size)]
        cols = [set() for _ in range(size)]
        boxes = [set() for _ in range(size)]

        for r in range(size):
            for c in range(size):

                digit = board[r][c]
                if digit == '.':
                    continue

                if digit not in digits:
                    return False

                box = (size//3) * (r // (size//3)) + (c // (size//3))
                if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                    return False
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)

        return True
