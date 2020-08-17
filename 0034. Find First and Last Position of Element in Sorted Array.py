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

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
# ```
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# ```
# Example 2:
# ```
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# ```

# # my solution 1, 类似二分搜索，分别找到此位置

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findfirst(left=0, right=len(nums)-1):
            if left>right:
                return -1
            mid = (left+right)//2
            if nums[mid] == target:
                if mid==0 or nums[mid-1]<target:
                    return mid
                return findfirst(left, mid-1)
            elif nums[mid] < target:
                return findfirst(mid+1, right)
            else:
                return findfirst(left, mid-1)
            
        def findlast(left=0, right=len(nums)-1):
            if left>right:
                return -1
            mid = (left+right)//2
            if nums[mid] == target:
                if mid==len(nums)-1 or nums[mid+1]>target:
                    return mid
                return findlast(mid+1, right)
            elif nums[mid] < target:
                return findlast(mid+1, right)
            else:
                return findlast(left, mid-1)
        
        return [findfirst(0, len(nums)-1),findlast(0, len(nums)-1)]


# # my solution 2, 简化

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary(target, left=0, right=len(nums)-1):
            if left > right:
                return left
            mid = (left+right)//2
            if nums[mid] >= target:
                return binary(target, left, mid-1)
            else:
                return binary(target, mid+1, right)
        lower = binary(target); higher = binary(target+1)
        return [lower,higher-1] if higher > lower else[-1,-1]


# # my solution 3, 修改jake‘s solution

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary(target, left, right):

            if left > right:
                return left

            mid = (left + right) // 2
            if target > nums[mid]:
                return binary(target, mid+1, right)
            else:
                return binary(target, left, mid-1)

        lower = binary(target - 0.5, 0, len(nums) - 1)
        upper = binary(target + 0.5, 0, len(nums) - 1)
        return [-1, -1] if lower == upper else [lower, upper - 1]


nums = [0,1,1,1,3]
target = 1
solution = Solution()
print(solution.searchRange(nums, target))


# # Jake's solution
# Search for target +/- 0.5 (not integer so not found) and return the index above this.
# If same index is returned for + and - 0.5 then target not found.
# Binary search could be implemented iteratively or use the bisect module.
#
# Time - O(log n)
#
# Space - O(1)

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary(target, left, right):

            if left > right:
                return left

            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

            return binary(target, left, right)

        lower = binary(target - 0.5, 0, len(nums) - 1)
        upper = binary(target + 0.5, 0, len(nums) - 1)
        return [-1, -1] if lower == upper else [lower, upper - 1]


nums = [0,1,1,1,3]
target = 1
solution = Solution()
print(solution.searchRange(nums, target))

if True:
    print(1)
if True:
    print(2)
else:
    print(3)
