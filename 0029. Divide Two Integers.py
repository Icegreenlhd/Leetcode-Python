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

# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
#
# Example 1:
# ```
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.
# ```
# Example 2:
# ```
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.
# ```

# my solution 1, time out
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        assert divisor != 0, "Divide the zero"
        sign = True if (dividend > 0) ^ (divisor > 0) else False
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            result += 1
            dividend -= divisor
        return -result if sign else result


# # Jake's solution
# Repeatedly double the divisor until it would exceed the dividend.  Then repeatedly halve the divisor, subtracting
# it from the dividend whenever possible.
# - Time - O(log n)
# - Space - O(1)
#

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return None
        diff_sign = (divisor < 0) ^ (dividend < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        max_divisor = divisor
        shift_count = 1

        while dividend >= (max_divisor << 1):   # find divisor * 2^i where divisor * 2^(i+1) > dividend
            max_divisor <<= 1
            shift_count <<= 1

        while shift_count >= 1:
            if dividend >= max_divisor:         # subtract max_divisor whenever possible
                dividend -= max_divisor
                result += shift_count
            shift_count >>= 1
            max_divisor >>= 1

        if diff_sign:
            result = -result
        return max(min(result, 2**31-1), -2**31)


True ^ True
