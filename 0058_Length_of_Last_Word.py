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

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a maximal substring consisting of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = s.split(" ")
        for i in range(len(s_list)-1, -1, -1):
            if len(s_list[i]) > 0:
                return len(s_list[i])
        else:
            return 0

# +
import unittest


class LeetcodeTest0057(unittest.TestCase):
    solution = Solution()

    def test_case1(self):
        test_input = "Hello world"
        test_output = 5
        self.assertEqual(self.solution.lengthOfLastWord(test_input), test_output)
        
    def test_case2(self):
        test_input = ""
        test_output = 0
        self.assertEqual(self.solution.lengthOfLastWord(test_input), test_output)
    
    def test_case3(self):
        test_input = "aaa"
        test_output = 3
        self.assertEqual(self.solution.lengthOfLastWord(test_input), test_output)

    def test_case4(self):
        test_input = "a "
        test_output = 1
        self.assertEqual(self.solution.lengthOfLastWord(test_input), test_output)

    def test_case5(self):
        test_input = "a aa"
        test_output = 2
        self.assertEqual(self.solution.lengthOfLastWord(test_input), test_output)


unittest.main(argv=['ignored', '-v'], exit=False)
