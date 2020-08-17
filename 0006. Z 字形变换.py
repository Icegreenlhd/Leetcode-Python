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

# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# ```python
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# ```
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
# 示例 1:
#
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 示例 2:
#
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# ```python
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
# ```
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zigzag-conversion
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# +
# my solution1
from collections import defaultdict


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        record = defaultdict(list)
        result = ''
        pointer = 0
        direct = 1

        for c in s:
            record[pointer].append(c)
            pointer += direct
            if pointer == numRows - 1 or pointer == 0:
                direct = -direct
                
#         for i, c in sorted(record.items()):
#             result += ''.join(c)

#         for _, z in record.items():
#             for c in z:
#                 print(c)
        return ''.join(c for _, z in record.items() for c in z)


# -

# my solution2
from collections import defaultdict
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        assert numRows >= 1, "wrong numRows"
        
        if numRows == 1:
            return s
        
        record = defaultdict(str)
        result = ''
        pointer = 0
        direct = 1
        
        for c in s:
            record[pointer] += c
            pointer += direct
            if pointer == numRows - 1 or pointer == 0:
                direct = -direct
        for i, c in record.items():
            result += c
        return result


# Jake solution
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        zigzag = [[] for _ in range(numRows)]
        row = 0
        direction = -1      # -1 for up, +1 for down

        for c in s:
            zigzag[row].append(c)
            if row == 0 or row == numRows-1:    # change direction
                direction = -direction
            row += direction

        return "".join([c for r in zigzag for c in r])  # flatten list of lists


#test1
s = 'PAYPALISHIRING'
numRows = 3 
solution = Solution()
solution.convert(s, numRows)

a = 1 
a = -a
a
