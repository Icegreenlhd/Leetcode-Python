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

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
# ```
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# ```
# Example 2:
# ```
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# ```

# my solution 1, 二分类递归
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(start, end):
            mid = int((start+end)/2)
            if start > end:
                return -1
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                if nums[start] == target:
                    return start
                elif nums[start] > nums[mid] and nums[start] < target:
                    return binary_search(start, mid-1)
                return binary_search(mid+1,end)
            else:
                if nums[end] == target:
                    return end
                elif nums[end] < nums[mid] and nums[end] > target:
                    return binary_search(mid+1,end)
                return binary_search(start,mid-1)
            
        if not nums:
            return -1
        
        return binary_search(0, len(nums)-1)


# my solution 2, 二分类递归，行数缩减版
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(start, end):
            mid = int((start+end)/2)
            if start > end:
                return -1
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                if nums[start] > nums[mid] and nums[start] <= target:
                    return binary_search(start, mid-1)
                return binary_search(mid+1, end)
            else:
                if nums[end] < nums[mid] and nums[end] >= target:
                    return binary_search(mid+1, end)
                return binary_search(start, mid-1)

        if not nums:
            return -1

        return binary_search(0, len(nums)-1)


# my solution 3, 二分类递归，类jake's solution
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(start, end):
            mid = int((start+end)/2)
            if start > end:
                return -1
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if target >= nums[start] and target <  nums[mid]:
                    return binary_search(start, mid-1)
                return binary_search(mid+1, end)
            else:
                if target <= nums[end] and target > nums[mid]:
                    return binary_search(mid+1, end)
                return binary_search(start, mid-1)

        if not nums:
            return -1

        return binary_search(0, len(nums)-1)


# +
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.

# Binary search.  If one side is sorted and target is in that region then rescurse on that side or else other side.
# Time - O(log n), half of the array is eliminated for every recursion.
# Space - O(1)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:  # LHS is sorted
                if target >= nums[left] and target < nums[mid]:  # target is on LHS
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # RHS is sorted
                if target <= nums[right] and target > nums[mid]:  # target is on RHS
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# -

nums = [3,1]
target = 1
solution = Solution()
print(solution.search(nums, target))
