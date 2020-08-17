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

# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# my result, not complete by myself, copy the idea and the implement code of Jack
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def get_median(start1, start2, k):
            assert k > 0, "k smaller than zero"
            assert k <= len(nums1) - start1 + len(nums2) - \
                start2, "k too large"
            if start1 >= len(nums1):
                return nums2[start2 + k - 1]
            if start2 >= len(nums2):
                return nums1[start1 + k - 1]
            if k == 1:
                return min(nums1[start1], nums2[start2])

            mid1, mid2 = float('inf'), float('inf')
            if k // 2 + start1 - 1 < len(nums1):
                mid1 = nums1[k // 2 + start1 - 1]
            if k // 2 + start2 - 1 < len(nums2):
                mid2 = nums2[k // 2 + start2 - 1]

            if mid1 < mid2:
                return get_median(start1 + k//2, start2, k - k//2)
            return get_median(start1, start2 + k//2, k - k//2)
        len1 = len(nums1)
        len2 = len(nums2)
        length = len1+len2
        right = get_median(0, 0, length//2+1)
        if length % 2:
            return right
        left = get_median(0, 0, length // 2)
        return (right + left) / 2.0


nums1 = [1,2,5]
nums2 = [3]
solution = Solution()
solution.findMedianSortedArrays(nums1, nums2)

nums1 = []
nums2 = []
solution = Solution()
solution.findMedianSortedArrays(nums1, nums2)
