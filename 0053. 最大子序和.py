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

# # my solution 1,滑动窗口法
# - Time - O(n)
# - Space - O(1)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, max_count = 0, float('-inf')
        for num in nums:
            count += num
            max_count = max(max_count, count)
            count = max(0, count)
        return max_count


# # my solution 2, 分治法, 写不出来
# - 

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def divide(nums, start, end, max_count):
            if start == 
            return divide(nums, start)
        


# # Jake's solution
# For each num calculate the max subarray sum ending with that num as either num alone (if previous sum was -ve) or
# num + previous sum (if previous sum was +ve)
# - Time - O(n)
# - Space - O(1)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        overall_max = float('-inf')
        max_ending_here = 0

        for num in nums:
            if max_ending_here > 0:
                max_ending_here += num
            else:
                max_ending_here = num
            overall_max = max(overall_max, max_ending_here)

        return overall_max
