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
#
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# - I can be placed before V (5) and X (10) to make 4 and 9. 
# - X can be placed before L (50) and C (100) to make 40 and 90. 
# - C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
# ```
# Input: 3
# Output: "III"
# ```
# Example 2:
# ```
# Input: 4
# Output: "IV"
# ```
# Example 3:
# ```
# Input: 9
# Output: "IX"
# ```
# Example 4:
# ```
# Input: 58
# Output: "LVIII"
#
# Explanation: L = 50, V = 5, III = 3.
# ```
# Example 5:
# ```
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# ```

# my solution 1
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        assert num > 0 and num < 4000, "out of rage"

        roman = ['I', "V", "X", "L", "C", "D", "M"]
        roman_index = 0
        roman_num = ''

        while(num):
            num_tmp = num % 10
            if num_tmp == 4:
                roman_num = roman[roman_index] + \
                    roman[roman_index+1] + roman_num
            elif num_tmp == 9:
                roman_num = roman[roman_index] + \
                    roman[roman_index+2] + roman_num
            elif num_tmp < 4:
                roman_num = roman[roman_index] * num_tmp + roman_num
            else:
                roman_num = roman[roman_index+1] + \
                    roman[roman_index] * (num_tmp-5) + roman_num
            num //= 10
            roman_index += 2

        return roman_num


# Jake's solution, map solution
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
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

        roman = []
        for i, numeral in mapping:
            while num >= i:
                num -= i
                roman.append(numeral)

        return "".join(roman)


input = []
input.append((3, "III"))
input.append((4, "IV"))
input.append((9,"IX"))
input.append((58,"LVIII"))
input.append((1994, "MCMXCIV"))
solution = Solution()
for i in input:
    num, result = i
    my_result = solution.intToRoman(num)
    if result != my_result:
        print("!Wrong", "Input:{} Result:{} Myresult:{}".format(num, result, my_result))
    else:
        print("Right", "Input:{} Result:{} Myresult:{}".format(num, result, my_result))
