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

# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为$[−2^{31},  2^{31} − 1]$。请根据这个假设，如果反转后整数溢出那么就返回 0。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-integer
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# my solution 1
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = -1 if x < 0 else 1
        x = abs(x)
        s = str(x)
        s = s[::-1]
        return int(s)*negative if abs(int(s)) <= 2**31 else 0


# Jake's solution
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0    # record if negative and change to positive
        x = abs(x)
        reversed = 0

        while x != 0:
            reversed = reversed * 10 + x % 10
            x //= 10

        if reversed > 2**31 - 1:    # required to pass leetcode test cases, not applicable for python
            return 0
        return reversed if not negative else -reversed


# test
x = -123
solution = Solution()
solution.reverse(x)

# test
x = 120
solution = Solution()
solution.reverse(x)

# test
x = 2**31 
solution = Solution()
solution.reverse(x)

2^30 -1
