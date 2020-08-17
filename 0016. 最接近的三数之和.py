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

# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# ```
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
# ```
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum-closest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# my solution 1 
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        close = float('inf')
        index = 0
        
        while index < len(nums) - 2:
            if index > 0 and nums[index] == nums[index-1]:  # certain no duplicate
                index += 1
                continue
            j = index + 1
            k = len(nums) - 1
            while j < k:
                # certain on duplicate
                triple_sum = nums[index] + nums[j] + nums[k]

                if triple_sum == target:
                    return target
                elif triple_sum > target:   
                    k -= 1
                else:              
                    j += 1
                if abs(close - target) > abs(triple_sum - target):
                    close = triple_sum

            index += 1
        return close


# +
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/3sum-closest/
# Given an array nums of n integers, find three integers in nums such that the sum is closest to a given number, target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Sort the array. For each staring index bidirectional search in the rest of the array.
# Time - O(n**2)
# Space - O(1)

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = float('inf')  # default if len(nums) < 3

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:

                triple = nums[i] + nums[j] + nums[k]
                if triple == target:    # early return, cannot do better
                    return target
                if abs(triple - target) < abs(closest - target):
                    closest = triple

                if triple - target > 0:
                    k -= 1
                else:
                    j += 1

        return closest


# -

# test
input = []
input.append(([-1,2,1,-4],1,2))
solution = Solution()
for i in input:
    num, target, result = i
    my_result = solution.threeSumClosest(num, target)
    if result != my_result:
        print("!Wrong", "Input:{}{} Result:{} Myresult:{}".format(
            num, target, result, my_result))
    else:
        print("Right", "Input:{}{} Result:{} Myresult:{}".format(
            num, target,result, my_result))
