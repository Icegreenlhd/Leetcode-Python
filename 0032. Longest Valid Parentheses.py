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

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# Example 1:
# ```
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# ```
# Example 2:
# ```
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# ```
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#my solution 1, stack + information reserve
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = list()
        count = 0
        maximum = 0
        
        for p in s:
            if p == '(':
                stack.append(count)
                count = 0
            elif p == ')':
                if not stack:
                    count = 0
                    continue
                count = count + 2 + stack.pop()
                maximum = max(count, maximum)
            else:
                raise Exception("Invalid element!", p)
        return maximum


# +
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-valid-parentheses/
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# For example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

# Maintain a stack of indices in s of unmatched brackets.  Pop an opening bracket when matched with a closing bracket.
# Push unmatched closing brackets and all opening brackets.  Then find the longest gap between indices on the stack.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []                  # indices of brackets that are not matched

        for i, c in enumerate(s):
            if c == ")" and stack and s[stack[-1]] == '(':
                stack.pop()         # close matches an open on the stack
            else:
                stack.append(i)     # puch open brackets or unmatched close brackets

        stack.append(len(s))        # last unmatched index after end of s
        max_length = stack[0]       # first unmatched index before start of s

        for index in range(1, len(stack)):  # find max gap between remaining unmatched indices
            max_length = max(max_length, stack[index] - stack[index-1] - 1)

        return max_length
