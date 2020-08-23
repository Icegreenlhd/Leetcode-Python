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

# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).  
#
# You may assume that the intervals were initially sorted according to their start times.  
#
# Example 1:  
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]  
# Output: [[1,5],[6,9]]  
# Example 2:  
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]  
# Output: [[1,2],[3,10],[12,16]]  
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].  
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.  


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        head, tail = [], []
        flag = True

        for interval in intervals:
            if interval[1] < newInterval[0] or interval[0] > newInterval[1]:
                if interval[0] > newInterval[1] and flag:
                    head.append(newInterval[0])
                    tail.append(newInterval[1])
                    flag = False
                head.append(interval[0])
                tail.append(interval[1])
            elif flag:
                head.append(min(interval[0], newInterval[0]))
                tail.append(max(interval[1], newInterval[1]))
                flag = False
            elif tail[-1] < interval[1]:
                tail[-1] = interval[1]
        if flag:
            head.append(newInterval[0])
            tail.append(newInterval[1])
        return [[head[_], tail[_]] for _ in range(len(head))]


# +
class Solution2(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        record = []
        flag = True

        for interval in intervals:
            if interval[1] < newInterval[0] or interval[0] > newInterval[1]:
                if interval[0] > newInterval[1] and flag:
                    record.append(newInterval)
                    flag = False
                record.append(interval)
            elif flag:
                record.append([min(interval[0], newInterval[0]), max(interval[1], newInterval[1])])
                flag = False
            elif record[-1][1] < interval[1]:
                record[-1][1] = interval[1]
        if flag:
            record.append(newInterval)
        return record


# +
import unittest


class LeetcodeTest0057(unittest.TestCase):
    solution = Solution2()

    def test_case1(self):
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        test_output = [[1, 2], [3, 10], [12, 16]]
        self.assertEqual(test_output, self.solution.insert(
            intervals, newInterval))

    def test_case2(self):
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        test_output = [[1, 5], [6, 9]]
        self.assertEqual(test_output, self.solution.insert(
            intervals, newInterval))

    def test_case3(self):
        intervals = [[1, 3], [6, 9]]
        newInterval = [0, 5]
        test_output = [[0, 5], [6, 9]]
        self.assertEqual(test_output, self.solution.insert(
            intervals, newInterval))

    def test_case4(self):
        intervals = []
        newInterval = [0, 5]
        test_output = [[0, 5]]
        self.assertEqual(test_output, self.solution.insert(
            intervals, newInterval))

    def test_case5(self):
        intervals = [[1, 5]]
        newInterval = [0, 0]
        test_output = [[0, 0], [1, 5]]
        self.assertEqual(test_output, self.solution.insert(
            intervals, newInterval))

    def test_case6(self):
        intervals = [[1, 5]]
        newInterval = [5, 5]
        test_output = [[1, 5]]
        self.assertEqual(test_output, self.solution.insert(
            intervals, newInterval))


unittest.main(argv=['ignored', '-v'], exit=False)
