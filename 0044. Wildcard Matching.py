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

# Given an input string (`s`) and a pattern (`p`), implement wildcard pattern matching with support for `'?'` and `'*'`.
# ```
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
# ```
# Note:
#
# - s could be empty and contains only lowercase letters a-z.
# - p could be empty and contains only lowercase letters a-z, and characters like `?` or `*`.
# Example 1:
# ```
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# ```
# Example 2:
# ```
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# ```
# Example 3:
# ```
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# ```
# Example 4:
# ```
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# ```
# Example 5:
# ```
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
# ```

# # my solution 1, 动态规划
# - Time：O($m n$)
# - Space: O($n^2$)

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dynamic = [[False for _ in range(len(s)+1)] for _ in range(len(p)+1)]
        dynamic[0][0] = True

        for i in range(1, len(p)+1):
            for j in range(len(s)+1):
                if p[i-1] == "*" and (dynamic[i-1][j] or (j > 0 and dynamic[i][j-1])):
                    dynamic[i][j] = True
                elif j>0 and dynamic[i-1][j-1] and (p[i-1] == "?" or p[i-1] == s[j-1]):
                    dynamic[i][j] = True
        return dynamic[len(p)][len(s)]
          


# # my solution 2, 根据0010修改

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dynamic = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dynamic[0][0] = True

        for i in range(len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == "*":
                    dynamic[i][j] = dynamic[i][j-1] or (i > 0 and dynamic[i-1][j])
                else:
                    dynamic[i][j] = i > 0 and dynamic[i-1][j-1] and (p[j-1] == '?' or p[j-1] == s[i-1])
        return dynamic[len(s)][len(p)]


# # Jake's solution
# Record index in p of star and index in s at that time.  Try to match without star, if fails back up and use *
# to match one more character from s.
# - Time - O(m * n), * at beginning of p could match many chars in s before failing and repeatedly backtrack
# - Space - O(1)

class Solution(object):
    def isMatch(self, s, p):

        i, j = 0, 0         # next indices to be matched in s and p
        star = -1           # last index in p of *

        while i < len(s):

            # if beyond end of pattern or pattern is unmatched letter
            if j >= len(p) or (p[j] not in {'*' , '?'} and p[j] != s[i]):
                if star == -1:      # no flexibility if no star
                    return False
                j = star + 1        # reset p to character after star
                star_i += 1         # reset s to charcater after star_i, i.e. use * to match one char from s
                i = star_i

            elif p[j] == '*':       # record * index in p and next index to be matched in s
                star = j
                star_i = i
                j += 1

            else:                   # chars match or ?, increment both
                i += 1
                j += 1

        while j < len(p):           # any remaining characters in p can only be *
            if p[j] != '*':
                return False
            j += 1
        return True
