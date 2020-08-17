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

# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#  
#
# 示例：
# ```
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
# ```
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# my solution1, time out
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        index = 0
        three = []

        while(index < len(nums) - 1 and nums[index] <= 0):
            if index > 0 and nums[index] == nums[index-1]:  # certain no duplicate
                index += 1
                continue
            add = index + 1
            end = len(nums) - 1
            while(add < len(nums)):
                # certain on duplicate
                if add > index+1 and nums[add] == nums[add-1]:
                    add += 1
                    continue
                another = -(nums[index] + nums[add])
                for i in range(end, add, -1):
                    if nums[i] <= another:
                        if nums[i] == another:
                            three.append([nums[index], nums[add], another])
                        break
                add += 1
            index += 1
        return three


# my solution2
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        index = 0
        three = []

        while index < len(nums) - 1 and nums[index] <= 0:
            if index > 0 and nums[index] == nums[index-1]:  # certain no duplicate
                index += 1
                continue
            j = index + 1
            k = len(nums) - 1
            while j < k:
                # certain on duplicate
                triple_sum = nums[index] + nums[j] + nums[k]

                if triple_sum == 0:
                    three.append([nums[index], nums[j], nums[k]])
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif triple_sum > 0:    # decrement k to next new number
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                else:                   # increment j to next new number
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

            index += 1
        return three


# +
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/3sum/
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# Note: The solution set must not contain duplicate triplets.

# Sort the array.  For each index i perform a bidirectional search on the higher values in the array.
# Skip over duplicates.  Increment i to the next new minimum number.
# Time - O(n**2), for each i at least one of j and k moves every iteration.
# Space - O(n)


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()

        i = 0
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1

            while j < k:

                triple_sum = nums[i] + nums[j] + nums[k]

                if triple_sum == 0:     # record result and move both j and k to next new numbers
                    results.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif triple_sum > 0:    # decrement k to next new number
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                else:                   # increment j to next new number
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

            i += 1                      # increment i to next new number
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1

        return results


# -

input = []
input.append(([-1, 0, 1, 2, -1, -4],
              [[-1, 0, 1],
               [-1, -1, 2]]))
input.append(([0,0,0,0,0,0],
              [[0,0,0]]))
solution = Solution()
for i in input:
    num, result = i
    my_result = solution.threeSum(num)
    result.sort(); my_result.sort()
    if result != my_result:
        print("!Wrong", "Input:{} Result:{} Myresult:{}".format(
            num, result, my_result))
    else:
        print("Right", "Input:{} Result:{} Myresult:{}".format(
            num, result, my_result))
