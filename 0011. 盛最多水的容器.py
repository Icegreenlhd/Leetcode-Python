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

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
# <img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" width="100%">
#
#
#
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
#
#  
#
# Example:
# ```
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# ```

# my solution 1, simple idea that just for traverse the height, timeout
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        output = 0

        for i in range(len(height)):
            for j in range(i, len(height)):
                width = j - i
                area = width * min(height[i], height[j])
                output = max(area, output)

        return output


# my solution 2,
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lowest = 0
        output = 0
        higher = [_ for _ in range(len(height)-1, -1, -1)]
        remove = []
        for i in range(len(height)):
            if i not in higher:
                continue
            higher.remove(i)
            for j in higher:
                if height[j] < lowest:
                    remove.append(j)
                    continue
                width = j - i
                lowest = max(min(height[i], height[j]), lowest)
                area = width * lowest
                output = max(area, output)
            while(remove):
                higher.remove(remove.pop())

        return output


# my solution 3, 短边补长
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        output = 0
        i, j, width = 0, len(height)-1, len(height)-1

        for _ in range(len(height)):
            output = max(output, width * min(height[i], height[j]))
            i, j, width = (i+1, j, width-1) if height[i] < height[j] else (i, j-1,width-1)

        return output


# Jake's solution
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max_area = (right - left) * min(height[right], height[left])

        while left < right:
            # By moving in the lower boundary we have the possibility
            if height[left] < height[right]:
                left += 1                       # of finding a larger area.
            else:
                right -= 1
            max_area = max(max_area, (right - left) *
                           min(height[right], height[left]))

        return max_area


# test
input = list()
input.append(([1, 8, 6, 2, 5, 4, 8, 3, 7], 49))
input.append(([1, 3, 2, 5, 25, 24, 5], 24))
input.append(([1, 2, 3, 4, 5, 25, 24, 3, 4], 24))
solution = Solution()
for i in input:
    height, result = i
    my_result = solution.maxArea(height)
    if result != my_result:
        print("Wrong", "Input:{} Result:{} Myresult:{}".format(
            height, result, my_result))
