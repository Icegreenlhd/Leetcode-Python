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
# Determine if you are able to reach the last index.
#
#
# **Example 1**:
#
# Input: nums = [2,3,1,1,4]  
# Output: true  
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.  
#
# **Example 2**:
#
# Input: nums = [3,2,1,0,4]  
# Output: false  
# Explanation: You will always arrive at index 3 no matter what. 
# Its maximum jump length is 0, which makes it impossible to reach the last index.
#
# Constraints:
#
# - $1 <= nums.length <= 3 * 10^4$
# - $0 <= nums[i][j] <= 10^5$


# my solution, dynamic programing
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        have_jump = 0
        can_jump = 1

        while can_jump > have_jump:
            max_jump = have_jump
            for i, j in enumerate(range(have_jump, can_jump)):
                max_jump = max(max_jump, have_jump+i+nums[j])
                if max_jump >= len(nums)-1:
                    return True
            can_jump, have_jump = max_jump+1, can_jump
        return False


# +
# unittest work on jupyter notebook
import unittest


class LeetcodeTest0055(unittest.TestCase):

    solution = Solution()

    def test_case1(self):
        nums = [2, 3, 1, 1, 4]
        output = True
        self.assertEqual(self.solution.canJump(nums), output)

    def test_case2(self):
        nums = [3, 2, 1, 0, 4]
        output = False
        self.assertEqual(self.solution.canJump(nums), output)

    def test_case3(self):
        nums = []
        output = False
        self.assertEqual(self.solution.canJump(nums), output)

    def test_case4(self):
        nums = [2, 0, 2, 0, 1]
        output = True
        self.assertEqual(self.solution.canJump(nums), output)


unittest.main(argv=['ignored', '-v'], exit=False)

