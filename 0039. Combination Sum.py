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

# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# - All numbers (including target) will be positive integers.
# - The solution set must not contain duplicate combinations.
# Example 1:
# ```
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# ```
# Example 2:
# ```
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
# ```

# # my solution1 , dynamic programming
#
# ## 学习点动态规划不适用于非求极值

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        assert all(candidates), "no zero input"
        dynamic = [[[] for t in range(target+1)]
                   for _ in range(len(candidates)+1)]
        for i, c in enumerate(candidates):
            for j in range(1, target+1):
                if j == c:
                    dynamic[i+1][j].append([c])
                if dynamic[i][j]:
                    for k in dynamic[i][j]:
                        dynamic[i+1][j].append(k[:])
                if j>c and dynamic[i+1][j-c]:
                    for k in dynamic[i+1][j-c]:
                        dynamic[i+1][j].append(k+[c])
        for i in dynamic:
            print(i)
        return dynamic[len(candidates)][target]


candidates = [2,3,4,5]
target = 8
solution= Solution()
solution.combinationSum(candidates, target)


# # Jake's Solution
# Subtract each candidate from target as many times as possible whilst remainder is non-negative. Recurse
# each time, moving on to the next candidate.
# - Time - approx f^n where f is target/average_candidate and n is the number of candidates with this nb recursions
#

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(candidates, 0, target, [], result)
        return result

    def helper(self, nums, next, target, partial, result):
        if target == 0:
            result.append(partial)
            return
        if next == len(nums):
            return

        i = 0
        while target-i*nums[next] >= 0:
            self.helper(nums, next+1, target-i *
                        nums[next], partial + [nums[next]]*i, result)
            i += 1


# # azl397985856 / leetcode 
# ## 思路
#
# 这道题目是求集合，并不是求极值，因此**动态规划**不是特别切合，因此我们需要考虑别的方法。
#
# 这种题目其实有一个通用的解法，就是**回溯法**。 网上也有大神给出了这种回溯法解题的 通用写法，这里的所有的解法使用通用方法解答。 除了这道题目还有很多其他题目可以用这种通用解法，具体的题目见后方相关题目部分。
#
# 我们先来看下通用解法的解题思路，我画了一张图：
# <img src='https://s1.ax1x.com/2020/05/15/YrIalR.png' width=70%>

class Solution:
    def combinationSum(self, candidates, target):
        """
        回溯法，层层递减，得到符合条件的路径就加入结果集中，超出则剪枝；
        主要是要注意一些细节，避免重复等；
        """
        size = len(candidates)
        if size <= 0:
            return []

        # 先排序，便于后面剪枝
        candidates.sort()

        path = []
        res = []
        self._find_path(target, path, res, candidates, 0, size)

        return res

    def _find_path(self, target, path, res, candidates, begin, size):
        """沿着路径往下走"""
        if target == 0:
            res.append(path[:])
        else:
            for i in range(begin, size):
                left_num = target - candidates[i]
                # 如果剩余值为负数，说明超过了，剪枝
                if left_num < 0:
                    break
                # 否则把当前值加入路径
                path.append(candidates[i])
                # 为避免重复解，我们把比当前值小的参数也从下一次寻找中剔除，
                # 因为根据他们得出的解一定在之前就找到过了
                self._find_path(left_num, path, res, candidates, i, size)
                # 记得把当前值移出路径，才能进入下一个值的路径
                path.pop()


candidates = [2,3,4,5]
target = 8
solution= Solution()
solution.combinationSum(candidates, target)
