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

# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
# ```
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
# ```

# my solution 1
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []

        nums.sort()
        i = 0
        quadruplets = []

        while i < len(nums) - 3:
            j = i+1

            while j < len(nums) - 2:
                k = j+1
                l = len(nums) - 1

                while k < l:

                    quadruple = nums[i] + nums[j] + nums[k] + nums[l]

                    if quadruple == target:
                        quadruplets.append(
                            [nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        l -= 1
                        while l > k and nums[l] == nums[l+1]:
                            l -= 1

                    elif quadruple < target:
                        k += 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1

                    else:
                        l -= 1
                        while l > k and nums[l] == nums[l+1]:
                            l -= 1

                j += 1
                while j < len(nums) - 2 and nums[j] == nums[j-1]:
                    j += 1

            i += 1
            while i < len(nums) - 3 and nums[i] == nums[i-1]:
                i += 1
        return quadruplets


# +
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/4sum/
# Given an array nums of n integers, are there elements a, b, c, and d in nums such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
# Note: The solution set must not contain duplicate quadruplets.

# Recursively reduce to 2sum problem.
# Time - O(n^3), for each pair perform linear search on the rest of the array

class Solution(object):
    ELEMENTS = 4        # parametrise the number of elements being summed

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        self.n_sum(sorted(nums), target, [], self.ELEMENTS, results)
        return results


    def n_sum(self, nums, target, partial, n, results):                 # generalise for n-sum

        if len(nums) < n or target > nums[-1]*n or target < nums[0]*n:  # early return if impossible
            return

        if n == 2:                      # base case of linear bidirectional search for n == 2
            left = 0
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target:
                    results.append(partial + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[right] == nums[right+1] and right > left:    # move to next different number if target found
                        right -=1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        else:
            for i in range(len(nums)-n+1):              # for all possible first numbers nums[i]
                if i == 0 or nums[i] != nums[i-1]:      # if not duplicate
                    self.n_sum(nums[i+1:], target-nums[i], partial + [nums[i]], n-1, results)
# -

# test
input = []
input.append(([1, 0, -1, 0, -2, 2], 0, [
    [-1,  0, 0, 1],
    [-2, -1, 1, 2],
    [-2,  0, 0, 2]
]))
input.append(([0,0,0,0,0,0,0,0], 0, [
    [0,  0, 0, 0]
]))
solution = Solution()
for i in input:
    nums, target, result = i
    my_result = solution.fourSum(nums, target)
    result.sort()
    my_result.sort()
    if result != my_result:
        print("!Wrong", "Input:{} Result:{} Myresult:{}".format(
            nums, result, my_result))
    else:
        print("Right", "Input:{} Result:{} Myresult:{}".format(
            nums, result, my_result))
