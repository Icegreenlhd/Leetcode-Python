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

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# ```
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# ```

# my solution 1, 
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        margin = len(nums) - 1  # 找到临界数，margin-1
        while margin > 0 and nums[margin] <= nums[margin - 1]:
            margin -= 1

        if margin == 0:
            nums.sort()
            return

        right = len(nums) - 1  # 找到临界右侧最小的大于临界数
        while right > margin and nums[right] <= nums[margin - 1]:
            right -= 1

        nums[margin-1], nums[right] = nums[right], nums[margin-1]
        nums[margin:] = sorted(nums[margin:])
        return


# my solution 2,simple modify
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        margin = len(nums) - 1  # 找到临界数，margin-1
        while margin > 0 and nums[margin] <= nums[margin - 1]:
            margin -= 1

        if margin > 0:
            right = len(nums) - 1  # 找到临界右侧最小的大于临界数
            while right > margin and nums[right] <= nums[margin - 1]:
                right -= 1
            nums[margin-1], nums[right] = nums[right], nums[margin-1]
        nums[margin:] = reversed(nums[margin:])
        return


# +
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/next-permutation/
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.

# Starting from the last number, move forward to find the first decrease nums[i].
# Find the smallest number bigger than nums[i], nums[j]. Swap nums[i] and nums[j].
# Reverse all from i+1 onwards, or whole array if no decrease found in first step.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return

        i = len(nums)-2     # starting at back, find the first decrease - increasing it will increment the permutation
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i != -1:         # if any decrease then find the smallest larger number to swap with
            j = i+1
            while j < len(nums) and nums[j] > nums[i]:
                j += 1
            j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # reverse all from i+1 onwards since they were decreasing and increasing minimises permutation
        left = i+1
        right = len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# -

nums = [1,5,1]
solution = Solution()
solution.nextPermutation(nums)
nums

array = [2,3,2,1]
array
a = array[1:]
a.reverse()
array[1:] = a
array
