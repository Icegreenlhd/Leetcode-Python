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

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
# ```
# Input: "()"
# Output: true
# ```
# Example 2:
# ```
# Input: "()[]{}"
# Output: true
# ```
# Example 3:
# ```
# Input: "(]"
# Output: false
# ```
# Example 4:
# ```
# Input: "([)]"
# Output: false
# ```
# Example 5:
# ```
# Input: "{[]}"
# Output: true
# ```

# my solution 1, 栈思路
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {'}': '{', ']': '[', ')': '('}
        stack = []
        index = 0
        while index < len(s):
            if parentheses.get(s[index]):
                if not stack or stack.pop() != parentheses[s[index]]:
                    return False
            else:
                stack.append(s[index])
            index += 1
        return True if not stack else False


# +
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-parentheses/
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# Maintain a stack of opening brackets.  For each closing bracket pop the head of the stack and check it matches.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {'(' : ')', '[' : ']', '{' : '}'}

        for c in s:
            if c in match:
                stack.append(c)
            else:
                if not stack or match[stack.pop()] != c:
                    return False

        return not stack


# -

# test
input = []
input.append(('()', True))
input.append(('()[]{}', True))
input.append(('(])', False))
input.append(('([)]', False))
input.append(('{[]}', True))
solution = Solution()
for i in input:
    s, result = i
    my_result = solution.isValid(s)
    if result != my_result:
        print("!Wrong", "Input:{} Result:{} Myresult:{}".format(s, result, my_result))
    else:
        print("Right", "Input:{} Result:{} Myresult:{}".format(s, result, my_result))
