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

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
# - All numbers (including target) will be positive integers.
# - The solution set must not contain duplicate combinations.
#
# Example 1:
# ```
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# ```
# Example 2:
# ```
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]
# ```

# # my solution 1, backtrack method
# use the collections.Counter to contain the number of the candidates

# +
from collections import Counter


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        candidates = list(Counter(candidates).items())
        res = []
        self.backtrack(candidates, target, 0, [], res)
        return res

    def backtrack(self, candidates, target, i, path, res):
        if target == 0:
            res.append(path[:])
            return
        else:
            for j in range(i, len(candidates)):
                left_num = target
                for _ in range(candidates[j][1]):
                    path.append(candidates[j][0])
                    left_num -= candidates[j][0]
                    if left_num < 0:
                        break
                    self.backtrack(candidates, left_num, j+1, path, res)
                for __ in range(_+1):
                    path.pop()


# -

candidates = [1,2,2,5]
target = 5
solution = Solution()
solution.combinationSum2(candidates,target)

# # my solution2, make up my fault
#
# backtrack method without collections

# +
from collections import Counter


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.backtrack(candidates, target, 0, [], res)
        return res

    def backtrack(self, candidates, target, i, path, res):
        if target == 0:
            res.append(path[:])
            return
        else:
            for j in range(i, len(candidates)):
                left_num = target - candidates[j]
                if left_num < 0:
                        break
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                path.append(candidates[j])  
                self.backtrack(candidates, left_num, j+1, path, res)
                path.pop()


# -

candidates = [1,2,2,5]
target = 5
solution = Solution()
solution.combinationSum2(candidates,target)

# # Jake's Solution
# Count the frequency of each number in candidates.  
#
# For each number subtract all possible numbers of copies up to
# the count and without exceeding target and recurse for the next number.
#
# Alternative iterative version below.
# - Time - O((f+1)^n) where f is the max frequency of any number and n is the number of distinct numbers

# +
from collections import Counter

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        freq = list(Counter(candidates).items())
        self.combos(freq, 0, target, [], results)
        return results

    def combos(self, freq, next, target, partial, results):
        if target == 0:
            results.append(partial)
            return
        if next == len(freq):
            return

        for i in range(freq[next][1]+1):
            if i * freq[next][0] > target:
                break
            self.combos(freq, next+1, target-i*freq[next][0], partial + [freq[next][0]]*i, results)


# Iterative version of same procedure.
class Solution_Iterative(object):
    def combinationSum2(self, candidates, target):
        results = []
        partials = [[]]
        freq = list(Counter(candidates).items())

        for candidate, count in freq:

            new_partials = []
            for partial in partials:

                partial_sum = sum(partial)
                for i in range(count + 1):
                    if partial_sum + candidate*i < target:
                        new_partials.append(partial + [candidate]*i)
                    elif partial_sum + candidate*i == target:
                        results.append(partial + [candidate]*i)
                    if partial_sum + candidate*i >= target:
                        break

            partials = new_partials

        return results


# -

# # azl397985856 / leetcode 
# ## 思路
#
# 这道题目是求集合，并不是求极值，因此**动态规划**不是特别切合，因此我们需要考虑别的方法。
#
# 这种题目其实有一个通用的解法，就是**回溯法**。 网上也有大神给出了这种回溯法解题的 通用写法，这里的所有的解法使用通用方法解答。 除了这道题目还有很多其他题目可以用这种通用解法，具体的题目见后方相关题目部分。
#
# 我们先来看下通用解法的解题思路，我画了一张图：
# <img src='https://s1.ax1x.com/2020/05/15/YrIalR.png' width=70%>
#
# ## 与39题的区别是不能重用元素，而元素可能有重复；
#         不能重用好解决，回溯的index往下一个就行；
#         元素可能有重复，就让结果的去重麻烦一些；

class Solution:
    def combinationSum2(self, candidates, target):
        """
        与39题的区别是不能重用元素，而元素可能有重复；
        不能重用好解决，回溯的index往下一个就行；
        元素可能有重复，就让结果的去重麻烦一些；
        """
        size = len(candidates)
        if size == 0:
            return []
        
        # 还是先排序，主要是方便去重
        candidates.sort()
        
        path = []
        res = []
        self._find_path(candidates, path, res, target, 0, size)
        
        return res
    
    def _find_path(self, candidates, path, res, target, begin, size):
        if target == 0:
            res.append(path[:])
        else:
            for i in range(begin, size):
                left_num = target - candidates[i]
                if left_num < 0:
                    break
                # 如果存在重复的元素，前一个元素已经遍历了后一个元素与之后元素组合的所有可能
                if i > begin and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                # 开始的 index 往后移了一格
                self._find_path(candidates, path, res, left_num, i+1, size)
                path.pop()


from collections import Counter
c = Counter(candidates)
print(c)
print(len(c))
print(c.keys())
c.items()
