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

# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
# ```
# Input: [1,2,0]
# Output: 3
# ```
# Example 2:
# ```
# Input: [3,4,-1,1]
# Output: 2
# ```
# Example 3:
# ```
# Input: [7,8,9,11,12]
# Output: 1
# ```
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.

# # my solution 1, 排序

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        m = 1
        for i in nums:
            if i == m:
                m += 1
        return m


# # Jake's solution
# If an element of nums is a positive integer that could appear in nums (1 to len(nums) inclusive) and is not in
# correct place (nums[i] = i+1) then swap.
# - Time - O(n)
# - Space - O(1)

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):

            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp

            i += 1

        for i, num in enumerate(nums):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
