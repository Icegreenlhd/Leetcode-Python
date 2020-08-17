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

# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
#
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：
#
# 如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
# 假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
# 该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。
#
# 在任何情况下，若函数不能进行有效的转换时，请返回 0 。
#
# 提示：
#
# 本题中的空白字符只包括空格字符 ' ' 。
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 $[−2^{31},  2^{31} − 1]$。如果数值超过这个范围，请返回  INT_MAX $(2^{31} − 1)$ 或 INT_MIN $(−2^{31})$ 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/string-to-integer-atoi
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# my solution1
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        negative = 1
        has_content = False
        INT_MIN = - 2 ** 31
        INT_MAX = 2 ** 31 -1
        
        for c in s:
            if has_content and not c.isdigit():
                break
            if c == ' ':
                continue
            if c.isdigit():
                result = result *10 + int(c)
            elif c == '-':
                negative = -1
            elif c != '+':
                break
            has_content = True
        if result > INT_MAX:
            return INT_MAX if negative == 1 else INT_MIN
        return result * negative


# my solution 2, change after watching Jake's solution
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        
        result = 0
        negative = 1
        has_content = False
        INT_MIN = - 2 ** 31
        INT_MAX = 2 ** 31 - 1

        if s and s[0] == '-':
            negative = -1
        if s and (s[0] == '+' or s[0] == '-'):
            s = s[1:]
        if not s:
            return 0

        for c in s:
            if not c.isdigit():
                break
            result = result * 10 + int(c)

        return max(min(result * negative, INT_MAX), INT_MIN)


# my solution 3, slice method, change after watching Jake's solution
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()

        result = 0
        negative = 1
        has_content = False
        INT_MIN = - 2 ** 31
        INT_MAX = 2 ** 31 - 1

        if s and s[0] == '-':
            negative = -1
        if s and (s[0] == '+' or s[0] == '-'):
            s = s[1:]
        if not s:
            return 0

        i = 0
        for i, c in enumerate(s):
            if not c.isdigit():
                i -= 1
                break
        result = int(s[:i+1]) if i+1 else 0

        return max(min(result * negative, INT_MAX), INT_MIN)


# Jake solution
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()       # remove padding spaces

        negative = False        # remove leading + or -
        if str and str[0] == '-':
            negative = True
        if str and (str[0] == '+' or str[0] == '-'):
            str = str[1:]
        if not str:
            return 0

        digits = {i for i in '0123456789'}
        result = 0
        for c in str:           # record integer upto first non-digit
            if c not in digits:
                break
            result = result * 10 + int(c)

        if negative:
            result = -result

        result = max(min(result, 2**31 - 1), -2**31)    # keep within 4 byte signed integer bounds
        return result


'2'.isdigit()
-2**31

# test
s = '    -42'
solution = Solution()
solution.myAtoi(s)

# test
s = 'word'
solution = Solution()
solution.myAtoi(s)

# test
s = '21154 akjda'
solution = Solution()
solution.myAtoi(s)

# test
s = '-2222222222'
solution = Solution()
solution.myAtoi(s)

# test
s = '+-1000'
solution = Solution()
solution.myAtoi(s)
