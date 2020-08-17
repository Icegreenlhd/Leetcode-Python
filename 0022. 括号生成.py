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

# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#  
#
# 示例：
# ```
# 输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
# ```
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/generate-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# my solution 1, recursion
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate(n, 0, '', result)
        return result
        
    def generate(self, n, left, prefix, result):
        if not n and not left:
            result.append(prefix)
            return
        if n:
            self.generate(n-1, left+1, prefix+'(', result)
        if left:
            self.generate(n, left-1, prefix+')',result)


# +
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/generate-parentheses/
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Recursively add an opening left bracket if any remain, and a closing right bracket if more left brackets have been used.
# Time - O(2^n), each recursion can generate 2 recursive calls althougn in practive this is an upper bound
# Space - O(2^n)

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate([], n, n, result)
        return result

    # Generates all parentheses given a starting prefix and remaining left and right brackets.
    def generate(self, prefix, left, right, result):
        if left == 0 and right == 0:
            result.append("".join(prefix))
        if left != 0:
            self.generate(prefix + ['('], left-1, right, result)
        if right > left:
            self.generate(prefix + [')'], left, right-1, result)


# -

input = []
input.append((3,[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]))
input.append((0,[
       ""
     ]))
solution = Solution()
for i in input:
    n, result = i
    my_result = solution.generateParenthesis(n)
    result.sort(); my_result.sort();
    if result != my_result:
        print("!Wrong", "Input:{} Result:{} Myresult:{}".format(n, result, my_result))
    else:
        print("Right", "Input:{} Result:{} Myresult:{}".format(n, result, my_result))
