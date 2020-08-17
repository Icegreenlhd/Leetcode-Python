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

# # my solution 1, 递归结合去重，类似0040
# - Time: O(n!)
# - Space: O(n!)

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        self.permute(nums, [], result)
        return result
    
    def permute(self, nums, particle, res):
        if not nums:
            res.append(particle[:])
            return
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            nums.pop(i)  
            self.permute(nums, particle+[n], res)
            nums.insert(i, n)


# # Jake's solution
#
# Count occurences of each unique number.  Recursively append each number if still has a positive count.
# - Time - O(n^2 * n!), as 046_Permutations if all numbers are unique
# - Space - O(n * n!)

# +
from collections import Counter

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        freq = Counter(nums)
        permutations = []
        self.permute_helper(len(nums), [], freq, permutations)
        return permutations

    def permute_helper(self, to_add, partial, freq, permutations):
        if to_add == 0:
            permutations.append(partial)

        for item in freq:
            if freq[item] > 0:
                freq[item] -= 1
                self.permute_helper(to_add-1, partial + [item], freq, permutations)
                freq[item] += 1


# +
nums = [3,3,0,3]
freq = Counter(nums)

solution = Solution()
result = solution.permuteUnique(nums)
