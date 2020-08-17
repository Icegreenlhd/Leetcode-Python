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

# # my solution 1
# - Time: $O(n!*n^2)$, n! result, each need adding n elements, addition taking O(n)
# - Space: $O(n*n!)$, result space

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = set(nums)
        result = []
        self.permution(nums, [], result)
        return result
    
    def permution(self, nums, partial, result):
        if not nums:
            result.append(partial[:])
            return 
        for i in nums:
            self.permution(nums-{i},partial+[i],result)


# # Jake's solution
# For each number, insert it at all possible places in all existing permutations.
# Alternatively recursively swap every index with every greater index (and itself).
# - Time - O($n^2 * n!$).  n! results, each of with has n elements added, each addition taking O(n) time for list slicing
# - Space - O(n *n!)

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = [[]]

        for num in nums:
            new_permutations = []
            for perm in permutations:
                for i in range(len(perm) + 1):
                    new_permutations.append(perm[:i] + [num] + perm[i:])
            permutations = new_permutations

        return permutations
