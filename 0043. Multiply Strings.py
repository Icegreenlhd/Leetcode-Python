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

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
# Example 1:
# ```
# Input: num1 = "2", num2 = "3"
# Output: "6"
# ```
# Example 2:
# ```
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# ```
# Note:
#
# - The length of both num1 and num2 is < 110.
# - Both num1 and num2 contain only digits 0-9.
# - Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# - You must not use any built-in BigInteger library or convert the inputs to integer directly.

# # my solution 1

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        count = 0
        multi = 1
        for i in range(len(num1)-1, -1, -1):
            mul = int(num1[i])
            multipler = multi
            for j in range(len(num2)-1,-1,-1):
                med = int(num2[j])
                count = count + mul*med*multipler 
                multipler *= 10
            multi *= 10
        return str(count)


# # Jake's solution
# Create a list of each digit in the result, starting wiht the least significant digit.
# Reverse input digit order. nums1[i] * nums2[j] is added to result[i+j+1] and result[i+j]
# Alternatively: return str(int(num1) * int(num2))
# - Time - O(m * n) where inputs are of lengths m and n
# - Space - O(max(m,n))
#

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]         # easier to work with lo
        
        result = [0] * (len(num1) + len(num2))


        for i in range(len(num1)):

            int1 = ord(num1[i]) - ord('0')

            for j in range(len(num2)):

                int2 = ord(num2[j]) - ord('0')

                tens, units = divmod(int1 * int2, 10)

                result[i + j] += units      # add units and handle carry of units
                if result[i + j] > 9:
                    result[i + j + 1] += result[i + j] // 10
                    result[i + j] %= 10

                result[i + j + 1] += tens   # add tens and handle carry of tens
                if result[i + j + 1] > 9:
                    result[i + j + 2] += result[i + j + 1] // 10
                    result[i + j + 1] %= 10

        while len(result) > 1 and result[-1] == 0:  # remove trailing zeros
            result.pop()
        return "".join(map(str, result[::-1]))      # reverse and convert to string

# ?divmod
# ?ord
