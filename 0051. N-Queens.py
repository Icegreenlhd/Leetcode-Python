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
#
# 示例:
# ```
# 输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# ```
#
# 提示：
# ```
# 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自 百度百科 - 皇后 ）
# ```
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/n-queens
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# # my solution 1, Greedy algorithm，copy Jake's solution

# my solution 1, Greedy algorithm，copy Jake's solution
class Solution(object):
    def solveNQueens(self, n):
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

        return [[''.join([['.', 'Q'] [col == board[row]] for col in range(n)]) for row in range(n)] for board in self.boards]
    
    def judge(self, num, new_col):
        for row, col in enumerate(self.boards[num]):
            if new_col == col: # same column
                return True
            if abs(new_col-col) == len(self.boards[num]) - row: # same diagonal
                return True
            
        return False


solution = Solution()
print(solution.solveNQueens(4))


# # my solution 2, DFS, Copy azl397985856 / leetcode
# > 结合DFS与位运算的大神级别操作

# my solution 2, DFS, Copy azl397985856 / leetcode
# 结合DFS与位运算的大神级别操作
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self.dfs(n)
        return self.res

    def dfs(self, n, row=0, cols=0, pie=0, na=0, partial=[]):
        if row >= n:
            self.res.append(partial)
            return
        bits = (~(cols | pie | na) & ((1 << n) - 1))
        while bits:
            p = bits & -bits
            self.dfs(n, row+1, cols | p, (pie | p) << 1, (na | p) >> 1, partial+[''.join([['.', 'Q'] [(1<<x) == p] for x in range(n)])])
            bits = bits & (bits - 1)


solution = Solution()
print(solution.solveNQueens(4))

# # Jake's solution, Greedy method

# +
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/n-queens/
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space respectively.

# For each column, place a queen in each possible row that does not conflict with an existing queen.
# Time - O(n^2 * n!), n possible rows for first col, n-1 for second ... etc.  each result size n^2
# Space - O(n^2 * n!)

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        partials = [[]]                         # solutions up to current row
        for col in range(n):
            new_partials = []
            for partial in partials:
                for row in range(n):
                    if not self.conflict(partial, row):
                        new_partials.append(partial + [row])
            partials = new_partials
        print(partials)
        results = []
        for partial in partials:                # convert result to strings
            result = [['.'] * n for _ in range(n)]
            for col, row in enumerate(partial):
                result[row][col] = 'Q'
            for row in range(n):
                result[row] = ''.join(result[row])
            results.append(result)

        return results

    def conflict(self, partial, new_row):
        for col, row in enumerate(partial):
            if new_row == row:                      # same row
                return True
            col_diff = len(partial) - col
            if abs(new_row - row) == col_diff:      # same diagonal
                return True

        return False


# -

# # Leetcode 官方回溯算法
# 链接：https://leetcode-cn.com/problems/n-queens/solution/nhuang-hou-by-leetcode/

class Solution:
    def solveNQueens(self, n):
        def could_place(row, col):
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])
        
        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1
        
        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0
        
        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)
        
        def backtrack(row = 0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)
        
        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack()
        return output


solution = Solution()
print(solution.solveNQueens(4))


# # ilove2yy DFS算法1
# 链接：https://leetcode-cn.com/problems/n-queens/solution/python-ji-jian-yi-zhu-by-iera/

class Solution(object):
    def solveNQueens(self, n):
        res = []
        if n == 0: return res
        # row为当前行，col为不可再使用的列，master为不可再使用的主对角线，slave为不可再使用的副对角线
        def dfs(row, col, master, slave, cur_res):
            if row == n:
                res.append(["." * cur + "Q" + "." * (n - cur - 1) for cur in cur_res])
                return
            for i in range(n):
                if (i not in col) and (i+row not in slave) and (i-row not in master):
                    dfs(row+1, col|{i}, master|{i-row}, slave|{i+row}, cur_res+[i])

        dfs(0, set(), set(), set(), [])
        return res


# # ZYK提供算法

# Solution given by ZYK
class Solution(object):
    def solveNQueens(self, n):
        self.result = []
        self.dfs(n, 0, [], [], [], [])
        return self.result

    def dfs(self, n, row=0,  col=[], summ=[], diff=[], res=[]):
        if row == n:
            self.result.append(res)
            return
        for i in range(n):
            if (i not in col) and (i + row not in summ) and (i - row not in diff):
                s = ''.join(['.','Q'] [x == i] for x in range(n))
                self.dfs(n, row+1,  col+[i], summ+[i+row], diff+[i-row], res+[s])
        return


solution = Solution()
print(solution.solveNQueens(4))
