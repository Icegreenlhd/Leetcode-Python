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

# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# 1. Each of the digits `1-9` must occur exactly once in each row.
# 2. Each of the digits `1-9` must occur exactly once in each column.
# 3. Each of the the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" width=30%>
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png" width=30%>
#
# Empty cells are indicated by the character `'.'`.
#
# Note:
#
# - The given board contain only digits 1-9 and the character '.'.
# - You may assume that the given Sudoku puzzle will have a single unique solution.
# - The given board size is always 9x9.

# # my solution 1, DFS 
#
# 将行列组成数，然后依次深度搜索

from copy import deepcopy
class Solution(object):
    size = 9
    res = None
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        size = self.size
        self.direct = list()
        digits = {str(i) for i in range(1,10)}
        rows = [digits.copy() for _ in range(size)]
        cols = [digits.copy() for _ in range(size)]
        boxes = [digits.copy() for _ in range(size)] 
        for r in range(size):
            for c in range(size):

                digit = board[r][c]
                
                if digit == ".":
                    self.direct.append(r*size+c)
                    continue
                    
                assert digit in digits, "invalid input: " + digit

                box = (size//3) * (r // (size//3)) + (c // (size//3))
                rows[r].remove(digit)
                cols[c].remove(digit)
                boxes[box].remove(digit)
                
        self.dfs(0, rows, cols, boxes, board)
        
        for n in self.direct: # in-place edit
            r = n // size
            c = n % size          
            board[r][c] = self.res[r][c]
#         for i in range(size):
#             board[i] = self.res[i]
        return 
    
    def dfs(self, n, rows, cols, boxes, board):
        if n == len(self.direct):
            self.res = deepcopy(board)
            return 
        size = self.size
        r = self.direct[n]//size
        c = self.direct[n]%size
        box = (size//3) * (r // (size//3)) + (c // (size//3))
        for num in rows[r] & cols[c] & boxes[box]:
            board[r][c] = num
            rows[r].remove(num)
            cols[c].remove(num)
            boxes[box].remove(num)
            self.dfs(n+1, rows, cols, boxes, board)
            board[r][c] = '.'
            rows[r].add(num)
            cols[c].add(num)
            boxes[box].add(num)


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solution = Solution()
solution.solveSudoku(board)
board


# # Jake's Solution
#
# Convert unknown cells to a set of possible digits, initially {1..9}.
# Repeatedly use known cells to eliminate possibilities in unknown cells.  Which creates new known cells etc.
# If this does not result in a solution, recursively guess each cell from its range of possibilities.

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.size = 9
        self.board = board
        # new digits at start or digits found by reducing to 1 possibility
        self.new_digits = []

        for r in range(self.size):
            # convert from string to list of digits
            self.board[r] = [digit for digit in self.board[r]]
            for c in range(self.size):
                if self.board[r][c] == '.':
                    # convert dot to set of possible digits
                    self.board[r][c] = {str(i) for i in range(1, 10)}
                else:
                    self.new_digits.append((r, c))

        while self.new_digits:  # use the certain number to delete the uncertain choice
            for r, c in self.new_digits:
                # given a new digit in (r,c), eliminate that digit from row, col and box
                self.eliminate(r, c)
                self.new_digits = []
                self.find_new()             # identify cells with only one possible digit

        self.solve_recursive()

    def eliminate(self, row, col):
        for i in range(self.size):

            if isinstance(self.board[i][col], set):
                # discard does not cause error if element not present
                self.board[i][col].discard(self.board[row][col])
            if isinstance(self.board[row][i], set):
                self.board[row][i].discard(self.board[row][col])

        for box_row in range(3*(row//3), 3 + 3*(row//3)):
            for box_col in range(3*(col//3), 3 + 3*(col//3)):
                if isinstance(self.board[box_row][box_col], set):
                    self.board[box_row][box_col].discard(self.board[row][col])

    def find_new(self):
        for row in range(self.size):
            for col in range(self.size):
                if isinstance(self.board[row][col], set) and len(self.board[row][col]) == 1:
                    self.board[row][col] = self.board[row][col].pop()
                    self.new_digits.append((row, col))

    def solve_recursive(self):

        for r in range(self.size):
            for c in range(self.size):

                if len(self.board[r][c]) == 1:
                    continue
                # loop over possible digits
                for digit in self.board[r][c]:
                    # will always be valid on first recursion
                    if self.is_valid(r, c, digit):
                        save_set = self.board[r][c]
                        self.board[r][c] = digit
                        if self.solve_recursive():
                            return True
                        self.board[r][c] = save_set     # revert back
                return False
        return True

    # checks whether board is valid after adding digit in row, col
    def is_valid(self, row, col, digit):
        for i in range(self.size):          # row and column
            if self.board[row][i] == digit or self.board[i][col] == digit:
                return False

        n = self.size // 3
        for r in range(n*(row//n), n + n*(row//n)):     # box
            for c in range(n*(col//n), n + n*(col//n)):
                if self.board[r][c] == digit:
                    return False
        return True


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solution = Solution()
solution.solveSudoku(board)
board

a = list(range(3))
set1 = set(a)
set2 = set(a)
print(set1)
set1.remove(0)
print(set1&set2)
print(set2)
print(set1-{2})
