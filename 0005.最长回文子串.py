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

# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 我的结果一，遇到错误：‘ababababababa'无法识别
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l1 = []
        l2 = []
        palin1 = []
        palin2 = []
        max_palin = [s[0]]
        for i, c in enumerate(s):
#             print(c)
#             print(i+1, "".join(max_palin))
#             print("".join(palin1))
            print(i+1, "".join(palin2))
            if palin1:
                if len(l1) == 0 or l1[-1] != c:
                    max_palin = palin1 if len(palin1) > len(
                        max_palin) else max_palin
                    l1 += palin1
                    palin1 = []
                else:
                    palin1.append(l1.pop())
                    palin1.insert(0, c)
            if not palin1:
                if len(l1) > 0 and l1[-1] == c:
                    palin1.append(l1.pop())
                    palin1.insert(0, c)
                else:
                    l1.append(c)
            if palin2:
                if len(l2) == 0 or l2[-1] != c:
                    max_palin = palin2 if len(palin2) > len(
                        max_palin) else max_palin
                    l2 += palin2
                    palin2 = []
                else:
                    palin2.append(l2.pop())
                    palin2.insert(0, c)
            if not palin2:
                if len(l2) > 1 and l2[-2] == c:
                    palin2.append(l2.pop())
                    palin2.append(l2.pop())
                    palin2.insert(0, c)
                else:
                    l2.append(c)
        max_palin = palin1 if len(palin1) > len(max_palin) else max_palin
        max_palin = palin2 if len(palin2) > len(max_palin) else max_palin
        return "".join(max_palin)


# my solution 2
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def get_palin(start, end):
            if start <= 0 or end >= len(s):
                return s[start: end]
            if s[start - 1] == s[end]:
                return get_palin(start - 1, end+1)
            else:
                return s[start: end]
        max_palin = ''
        for i, c in enumerate(s):
            odd = get_palin(i, i+1)
            max_palin = odd if len(odd) > len(max_palin) else max_palin
            if i >= 1 and s[i-1] == c:
                even = get_palin(i-1, i+1)
                max_palin = even if len(even) > len(max_palin) else max_palin
        return max_palin


# Jake solution
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""

        # create list of 2n-1 possible centres, each letter and between each pair
        # even indices represent letters, odd represent between letters
        # start with middle index that potentially creates longest palindrome
        centres = [len(s) - 1]
        for diff in range(1, len(s)):  # build list of indices from long to short
            centres.append(centres[0] + diff)
            centres.append(centres[0] - diff)
        print(centres)

        for centre in centres:

            if (min(centre + 1, 2 * len(s) - 1 - centre) <= len(longest)):
                break  # return if cannot make a longer palindrome

            if centre % 2 == 0:
                left, right = (centre // 2) - 1, (centre // 2) + 1
            else:
                left, right = centre // 2, (centre // 2) + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # left and right are now beyond the ends of the substring

            if right - left - 1 > len(longest):
                longest = s[left + 1:right]

        return longest


# Jake solution
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""

        def get_palin(start, end):
            if start < 0 or end >= len(s):
                return s[start+1: end]
            if s[start] == s[end]:
                return get_palin(start - 1, end+1)
            else:
                return s[start+1: end]

        # create list of 2n-1 possible centres, each letter and between each pair
        # even indices represent letters, odd represent between letters
        # start with middle index that potentially creates longest palindrome
        centres = [len(s) - 1]
        for diff in range(1, len(s)):  # build list of indices from long to short
            centres.append(centres[0] + diff)
            centres.append(centres[0] - diff)
#         print(centres)

        for centre in centres:

            if (min(centre + 1, 2 * len(s) - 1 - centre) <= len(longest)):
                break  # return if cannot make a longer palindrome

            if centre % 2 == 0:
                left, right = (centre // 2) - 1, (centre // 2) + 1
            else:
                left, right = centre // 2, (centre // 2) + 1

            palin = get_palin(left, right)
            longest = palin if len(palin) > len(longest) else longest
        return longest


l = ['a', 'a']
l[-1]
# l.pop()
l.insert(0, 1)
l[-1]
l

l = ['a', 'a']
''.join(l)

s = 'aaaaa'
solution = Solution()
solution.longestPalindrome(s)

s = 'aba'
solution = Solution()
solution.longestPalindrome(s)

s = 'ababababababa'
solution = Solution()
solution.longestPalindrome(s)

s = ''
solution = Solution()
solution.longestPalindrome(s)

s = 'a'
solution = Solution()
solution.longestPalindrome(s)
