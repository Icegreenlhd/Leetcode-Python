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

# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
# ```
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# ```
# 示例 2:
# ```
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# ```
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-common-prefix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# my solution 1
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def findCommonPrefix(str1, str2):
            commonprefix = ""
            if not str1 or not str2:
                return commonprefix
            for i in range(min(len(str1), len(str2))):
                if str1[i] == str2[i]:
                    commonprefix += str1[i]
                else:
                    return commonprefix
            return commonprefix
        
        if not strs:
            return ""
        commonprefix = strs[0]

        for i in range(1, len(strs)):
            commonprefix = findCommonPrefix(commonprefix, strs[i])

        return commonprefix


# Jake's solution
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        strs.sort()
        first = strs[0]
        last = strs[-1]

        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]


input = []
input.append((["flower","flow","flight"], "fl"))
input.append((["dog","racecar","car"], ""))
input.append(([], ""))
solution = Solution()
for i in input:
    strs, result = i
    my_result = solution.longestCommonPrefix(strs)
    if result != my_result:
        print("!Wrong", "Input:{} Result:{} Myresult:{}".format(strs, result, my_result))
    else:
        print("Right", "Input:{} Result:{} Myresult:{}".format(strs, result, my_result))
