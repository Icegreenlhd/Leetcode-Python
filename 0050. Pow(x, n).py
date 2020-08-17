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

# # my solution 1，简单乘积

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        x = 1/x if n < 0 else x
        
        newx = x
        for _ in range(abs(n)-1):
            newx *= x
            
        return newx


# # Jake solution
# Recursively calculate (pow(x, n//2))^2 if n is even or with additional factor of x if n is odd.
# - Time - O(log n)
# - Space - O(log n)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        neg = n < 0
        pos_result = self.pos_pow(x, abs(n))
        return 1/pos_result if neg else pos_result

    def pos_pow(self, x, n):
        if n == 0:
            return 1

        temp = self.pos_pow(x, n//2)
        temp *= temp

        return temp if n % 2 == 0 else temp * x
