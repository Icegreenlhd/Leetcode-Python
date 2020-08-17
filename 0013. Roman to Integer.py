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

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# ```
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# ```
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# - I can be placed before V (5) and X (10) to make 4 and 9. 
# - X can be placed before L (50) and C (100) to make 40 and 90. 
# - C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
# ```
# Input: "III"
# Output: 3
# ```
# Example 2:
# ```
# Input: "IV"
# Output: 4
# ```
# Example 3:
# ```
# Input: "IX"
# Output: 9
# ```
# Example 4:
# ```
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# ```
# Example 5:
# ```
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# ```

# my solution
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = [(1000, 'M'),
                   (900, 'CM'),
                   (500, 'D'),
                   (400, 'CD'),
                   (100, 'C'),
                   (90, 'XC'),
                   (50, 'L'),
                   (40, 'XL'),
                   (10, 'X'),
                   (9, 'IX'),
                   (5, 'V'),
                   (4, 'IV'),
                   (1, 'I'), ]

        num = 0
        left = 0
        for i, symbol in mapping:
            while len(s) >= len(symbol)+left and s[left: left+len(symbol)] == symbol:
                num += i
                left += len(symbol)

        return num


# Jake's solution, idea similar
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        doubles = {'CM' : 900, 'CD' : 400, 'XC' : 90, 'XL' : 40, 'IX' :9, 'IV' : 4}
        singles = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}

        integer = 0
        i = 0
        while i < len(s):
            if i < len(s)-1 and s[i:i+2] in doubles:
                integer += doubles[s[i:i+2]]
                i += 2
            else:
                integer += singles[s[i]]
                i += 1

        return integer


# test
input = []
input.append(('III', 3))
input.append(('IV', 4))
input.append(('IX', 9))
input.append(('LVIII', 58))
input.append(('MCMXCIV', 1994))
input.append(("MMCCCXCIX", 2399))
solution = Solution()
for i in input:
    s, result = i
    my_result = solution.romanToInt(s)
    if result != my_result:
        print("!Wrong", "Input:{} Result:{} Myresult:{}".format(s, result, my_result))
    else:
        print("Right", "Input:{} Result:{} Myresult:{}".format(s, result, my_result))
