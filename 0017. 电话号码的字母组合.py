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

# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
# <img src = "https://assets.leetcode-cn.com/aliyun-lc-upload/original_images/17_telephone_keypad.png"
# width= "50%">
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# my solution 1, 循环
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        digit_map = {2: ['a', 'b', 'c'],
                     3: ['d', 'e', 'f'],
                     4: ['g', 'h', 'i'],
                     5: ['j', 'k', 'l'],
                     6: ['m', 'n', 'o'],
                     7: ['p', 'q', 'r', 's'],
                     8: ['t', 'u', 'v'],
                     9: ['w', 'x', 'y', 'z']}
        result = [""]
        
        for digit in digits:
            assert digit_map.get(int(digit)), "not in digit map"
            temp = result[:]
            result = []
            for prefix in temp:
                for suffix in digit_map[int(digit)]:
                    result.append(prefix+suffix)
                    
        return result


# my solution 2, 递归
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        digit_map = {2: ['a', 'b', 'c'],
                     3: ['d', 'e', 'f'],
                     4: ['g', 'h', 'i'],
                     5: ['j', 'k', 'l'],
                     6: ['m', 'n', 'o'],
                     7: ['p', 'q', 'r', 's'],
                     8: ['t', 'u', 'v'],
                     9: ['w', 'x', 'y', 'z']}
        result = []

        def lettercombine(index, prefix):
            if index >= len(digits):
                result.append(prefix)
            else:
                assert digit_map.get(int(digits[index])), "not in digit map"
                for suffix in digit_map[int(digits[index])]:
                    lettercombine(index+1, prefix+suffix)
        lettercombine(0, '')
        return result


# +
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Given a digit string, return all possible letter combinations that the number could represent.

# For each digit add all possible letter mappings to each of the previous results.
# Alternatively can be solved recursively.
# Time - O(n * 4^n)
# Space - O(n * 4^n), max 4 possible chars per digit so O(4^n) strings each of length n

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits or '0' in digits or '1' in digits:
            return []

        results = [[]]
        mapping = {'2' : ['a', 'b', 'c'],
                   '3' : ['d', 'e', 'f'],
                   '4' : ['g', 'h', 'i'],
                   '5' : ['j', 'k', 'l'],
                   '6' : ['m', 'n', 'o'],
                   '7' : ['p', 'q', 'r', 's'],
                   '8' : ['t', 'u', 'v'],
                   '9' : ['w', 'x', 'y' , 'z']}

        for digit in digits:
            temp = []
            for result in results:
                for letter in mapping[digit]:
                    temp.append(result + [letter])
            results = temp

        # convert lists of chars to strings
        return ["".join(result) for result in results]


# -

input = []
input.append(("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]))
solution = Solution()
for i in input:
    digits, result = i
    my_result = solution.letterCombinations(digits)
    if result != my_result:
        print("!Wrong", "Input:{} Result:{} Myresult:{}".format(
            digits, result, my_result))
    else:
        print("Right", "Input:{} Result:{} Myresult:{}".format(
            digits, result, my_result))


