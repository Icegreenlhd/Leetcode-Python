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

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
# ```
# Input: [1,3,5,6], 5
# Output: 2
# ```
# Example 2:
# ```
# Input: [1,3,5,6], 2
# Output: 1
# ```
# Example 3:
# ```
# Input: [1,3,5,6], 7
# Output: 4
# ```
# Example 4:
# ```
# Input: [1,3,5,6], 0
# Output: 0
# ```

# # my solution1, iterable

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


# # my solution2, recursive

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def search(left, right):
            if left > right:
                return left
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return search(left, mid-1)
            else:
                return search(mid+1, right)
            
        return search(0, len(nums)-1)


nums = [1,3,5,6]
target = 7
solution = Solution()
solution.searchInsert(nums, target)
