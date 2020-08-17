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

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
# ![trapping rain water](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. **Thanks Marcos** for contributing this image!
#
#
# Example:
# ```python
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# ```

# # my solution 1,遍历一遍height
# 下降的index保存。
# 启动项-上升时判断是否存在有下降的index：
# 1. 存在：
#  1. 比它高（上升空间有余）：保存其高度作为下一次高度差计算
#  2. 比它低或一样高（上升空间不足）退出循环
#      - 比它低则保留下降的index
# 2. 不存在跳过
#
# **复杂度计算**：
#
# - Time-O(n)
# - Space-O(n)

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        index = 0
        down = []
        count = 0
        while index < len(height):
            if index > 0 and height[index] > height[index-1]: # 上升
                available = 0
                while down:
                    last = down.pop()
                    count = count + (min(height[last], height[index])-max(height[index-1], available))*(index-last-1)
                    if height[index] > height[last]:# 上升仍有空间
                        available = height[last]
                    else:  # 上升能力不足
                        if height[last] > height[index]:  # 保留多余的下降能力
                            down.append(last)
                        break
                        
            if index < len(height)-1 and height[index] > height[index+1]:  # 下降
                down.append(index)
            index += 1
        return count


height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution()
solution.trap(height)


# # Jake's Solution
# Calculate the highest elevation to the right and to the left of every bar.  Min of these is the max depth of water.
# Subtract the bar height from the max possible depth and floor at zero.
# - Time - O(n)
# - Space - O(n)

class Solution(object):
    def trap(self, height):

        highest_right = [0] * len(height)
        for i in range(len(height)-2, -1, -1):
            highest_right[i] = max(highest_right[i+1], height[i+1])

        highest_left, depth = [0] * len(height), 0
        for i in range(1, len(height)):     # depth[0] will be 0 so ok for range to start at 1
            highest_left[i] = max(highest_left[i-1], height[i-1])
            depth += max(0, min(highest_left[i], highest_right[i]) - height[i])

        return depth


[2,1,0,2]
[4,2,0,3,2,5]
