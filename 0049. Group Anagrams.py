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

# # my solution 1, 以dict解
# 缺陷为结果中字符串中有相同的字符会放在一起，

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for i in strs:
            letter_list = list(i)
            letter_list.sort()
            sorted_i = "".join(letter_list)
            if res.get(sorted_i):
                res[sorted_i].append(i)
            else:
                res[sorted_i]= [i]
        return list(res.values())


# # Jake's solution
# Sort the letters in each word.  Use sorted words as dictionary keys, values are unsorted words.
# Anagrams have equivalent sorted words.
# - Time - O(k log k * n) for n words of length k
# - Space - O(k * n)

# +
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_words = defaultdict(list)

        for word in strs:
            letter_list = list(word)
            letter_list.sort()
            sorted_word = "".join(letter_list)
            sorted_words[sorted_word].append(word)

        return list(sorted_words.values())


# -

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
print(solution.groupAnagrams(input))

list("ead") == list("eda")

a1 = [2,1]
a2 = [2,3]
set(a1)^set(a2)
