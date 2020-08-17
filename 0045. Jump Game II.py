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

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
# ```
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.
# ```
# Note:
#
# You can assume that you can always reach the last index.

# # my solution 1, dynamic algorithm
#
# - Time:O(n!)
#   - Time out
# - Space:O(n)

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dynamic = [float("inf") for _ in range(len(nums))]
        dynamic[0] = 0
        
        for i, n in enumerate(nums):
            for j in range(i+1, min(len(nums), n+i+1)):
                dynamic[j] = min(dynamic[j], dynamic[i]+1)
                if j == len(nums)-1:
                    return dynamic[j]
        return dynamic.pop()


# # my solution 2,  greedy algorithm
# - Time: O(n)
# - Space: O(n)

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_jump = 0
        candidates = [0]
        jump_times = 0
        
        while candidates:
            if max_jump >= len(nums)-1:
                return jump_times
            max_jump = last_jump
            for c in candidates:
                max_jump = max(nums[c]+c, max_jump)
            candidates = list(range(last_jump+1, max_jump+1))
            last_jump = max_jump
            jump_times += 1
            
        assert False, "can not jump to the result"
        return jump_times


# modify
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_jump = 0
        candidates = [0]
        jump_times = 0
        max_jump = last_jump
        
        while candidates:
            if last_jump >= len(nums)-1:
                return jump_times
            for c in candidates:
                max_jump = max(nums[c]+c, max_jump)
            candidates = list(range(last_jump+1, max_jump+1))
            last_jump = max_jump
            jump_times += 1
            
        assert False, "can not jump to the result"


# # Jake's Solution
# For each index in currently accessible range, update the max_index that can be reached in one more step.
# Iterate to next range, from end of previous range to max_index.
# - Time - O(n)
# - Space - O(1)

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        start, end = 0, 0   # indices in nums of current range
        max_index = 0
        steps = 1

        while True:         # will always terminate since last index is accessible
            for i in range(start, end+1):
                max_index = max(max_index, i + nums[i])
            if max_index >= len(nums)-1:
                return steps
            steps += 1
            start, end = end + 1, max_index


1 < float("inf")
