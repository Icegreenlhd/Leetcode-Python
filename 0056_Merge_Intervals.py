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

# ### Medium  
# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]  
# Output: [[1,6],[8,10],[15,18]]  
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].  
# Example 2:  
#
# Input: intervals = [[1,4],[4,5]]  
# Output: [[1,5]]  
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.  
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.  
#
# Constraints:  
#
# intervals[i][0] <= intervals[i][1]
#


# my solution
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        record = []
        for i in intervals:
            for j in range(len(record)):
                if record[j][0] <= i[0] <= record[j][1]:
                    if record[j][1] < i[1]:
                        record[j][1] = i[1]
                    break
            else:
                record.append(i[:])
        return record


# +
import unittest


class LeetcodeTest0056(unittest.TestCase):
    solution = Solution()

    def test_case1(self):
        test_input = [[1, 3], [2, 6], [8, 10], [15, 18]]
        test_output = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(self.solution.merge(test_input), test_output)

    def test_case2(self):
        test_input = [[1, 4], [4, 5]]
        test_output = [[1, 5]]
        self.assertEqual(self.solution.merge(test_input), test_output)

    def test_case3(self):
        test_input = [[1, 3], [2, 5], [4, 6]]
        test_output = [[1, 6]]
        self.assertEqual(self.solution.merge(test_input), test_output)

    def test_case4(self):
        test_input = [[1, 3], [7, 9], [6, 8]]
        test_output = [[1, 3], [6, 9]]
        self.assertEqual(self.solution.merge(test_input), test_output)

    def test_case5(self):
        test_input = [[1, 3], [3, 5]]
        test_output = [[1, 5]]
        self.assertEqual(self.solution.merge(test_input), test_output)

    def test_case6(self):
        test_input = [[1, 5], [3, 5]]
        test_output = [[1, 5]]
        self.assertEqual(self.solution.merge(test_input), test_output)

    def test_case7(self):
        test_input = [[1, 5], [7, 9], [5, 7]]
        test_output = [[1, 9]]
        self.assertEqual(self.solution.merge(test_input), test_output)

    def test_case8(self):
        test_input = [[1, 5]]
        test_output = [[1, 5]]
        self.assertEqual(self.solution.merge(test_input), test_output)

    def test_case9(self):
        test_input = [[0, 0]]
        test_output = [[0, 0]]
        self.assertEqual(self.solution.merge(test_input), test_output)


unittest.main(argv=['ignored', '-v'], exit=False)
