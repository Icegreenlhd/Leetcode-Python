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

# The count-and-say sequence is the sequence of integers with the first five terms as following:
# ```
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# ```
# `1 `is read off as `"one 1"` or `11`.
#
# `11` is read off as `"two 1s"` or `21`.
#
# `21` is read off as `"one 2`, then `one 1"` or `1211`.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the $n^{th}$ term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
#  
#
# Example 1:
#
# Input: 1
# Output: "1"
# Explanation: This is the base case.
# Example 2:
#
# Input: 4
# Output: "1211"
# Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".

# # my solution1 , recursively solved the problem

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def say(i, s):
            if i == n:
                return s
            count = 0
            new_s = ""
            num = s[0]
            for number in s:
                if number != num:
                    new_s = new_s + str(count) + num
                    num = number
                    count = 0
                count += 1
            new_s = new_s + str(count) + num
            return say(i+1, new_s)

        return say(1, "1")


n = 30
solution = Solution()
print(solution.countAndSay(n))


# # Jake's solution
# Iterate through the previous sequence.  When we see a different number, append [1, num] to the new sequence.
# When we see the same number increment its count.
# - Time - O(2^n), the sequence at worst doubles each step
# - Space - O(2^n)

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        sequence = [1]
        for _ in range(n-1):
            next = []
            for num in sequence:
                if not next or next[-1] != num:
                    next += [1, num]
                else:
                    next[-2] += 1
            sequence = next

        return "".join(map(str, sequence))


import itertools
list(itertools.starmap(pow,[(3,2),(111,1)]))
