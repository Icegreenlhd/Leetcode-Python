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

# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# <img src="https://assets.leetcode.com/uploads/2018/10/12/8-queens.png" width=50%>
#
# 上图为 8 皇后问题的一种解法。
#
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#

# my solution 1, Greedy algorithm，copy Jake's solution
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.boards = [[]]
        
        for row in range(n):
            new_boards = []
            for num in range(len(self.boards)):
                for col in range(n):
                    if not self.judge(num, col):
                        new_boards.append(self.boards[num] + [col])
            del self.boards
            self.boards = new_boards

        return len(self.boards)
    
    def judge(self, num, new_col):
        for row, col in enumerate(self.boards[num]):
            if new_col == col: # same column
                return True
            if abs(new_col-col) == len(self.boards[num]) - row: # same diagonal
                return True
            
        return False


solution = Solution()
print(solution.totalNQueens(4))


# my solution 2, DFS, Copy azl397985856 / leetcode
# 结合DFS与位运算的大神级别操作
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = 0
        self.dfs(n, 0, 0, 0, 0)
        return self.res

    def dfs(self, n, row, cols, pie, na):
        if row >= n:
            self.res += 1
            return
        bits = (~(cols | pie | na) & ((1 << n) - 1))
        while bits:
            p = bits & -bits
            bits = bits & (bits - 1)
            self.dfs(n, row+1, cols | p, (pie | p) << 1, (na | p) >> 1)
