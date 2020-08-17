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

# # my solution 1, recursion 
# - Time: O(2^n)

class Solution(object):
    result = 0
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.climb(n)
        return self.result
    
    def climb(self, n):
        if n <= 0:
            self.result = self.result + 1 if n == 0 else self.result
            return 
        
        for i in range(1,3):
            self.climbStairs(n-i)
            


# # Jake's solution
# Dynamic programming.  Base cases of no ways for n <= 0, 1 way for n == 1 and 2 ways for n == 2.
# For each additional step, the number of ways is taking one step from the previous step + taking two steps from the
# step before that. Result is a Fibonacci sequence.
# - Time - O(n)
# - Space - O(1)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 2:
            return n

        stairs, prev = 2, 1         # 2 ways to reach second step, one way to reach first
        for _ in range(3, n + 1):
            stairs, prev = stairs + prev, stairs

        return stairs
