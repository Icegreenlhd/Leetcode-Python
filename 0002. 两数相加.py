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

# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# +
# my solution
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = l1.val + l2.val
        carry = temp // 10
        result = l_temp = ListNode(temp % 10)

        while l1.next or l2.next or carry:
            if l1.next:
                l1 = l1.next
            else:
                l1.val = 0
            if l2.next:
                l2 = l2.next
            else:
                l2.val = 0
                
            temp = l2.val + l1.val + carry
            carry = temp // 10
            l_temp.next = ListNode(temp % 10)
            l_temp = l_temp.next
        return result


# +
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev = result = ListNode(None)      # dummy head
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry % 10)
            prev = prev.next
            carry //= 10
        
        return result.next


# -

# 作者：wang_ni_ma
# 链接：https://leetcode-cn.com/problems/add-two-numbers/solution/dong-hua-yan-shi-2-liang-shu-xiang-jia-by-user7439/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 王尼玛 解法1
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # 定义一个进位标志
        a, b, p, carry = l1, l2, None, 0
        while a or b:
            # a和b节点的值相加，如果有进位还要加上进位的值
            val = (a.val if a else 0)+(b.val if b else 0)+carry
            # 根据val判断是否有进位,不管有没有进位，val都应该小于10
            carry, val = val/10 if val >= 10 else 0, val % 10
            p, p.val = a if a else b, val
            # a和b指针都前进一位
            a, b = a.next if a else None, b.next if b else None
            # 根据a和b是否为空，p指针也前进一位
            p.next = a if a else b
        # 不要忘记最后的边界条件，如果循环结束carry>0说明有进位需要处理这个条件
        if carry:
            p.next = ListNode(carry)
        # 每次迭代实际上都是将val赋给a指针的，所以最后返回的是l1
        return l1


# 作者：wang_ni_ma
# 链接：https://leetcode-cn.com/problems/add-two-numbers/solution/dong-hua-yan-shi-2-liang-shu-xiang-jia-by-user7439/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 王尼玛 解法2 递归思路
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # 主要逻辑都在内部函数中实现
        def add(a, b, carry):
            # 递归的终止条件是a和b都为空
            # 如果carry大于0需要返回一个进位标志
            if not (a or b):
                return ListNode(1) if carry else None
            # 如果a为空则将ListNode(0)赋给a，对于b也是
            a = a if a else ListNode(0)
            b = b if b else ListNode(0)
            # 处理val，以及进位标志
            val = a.val + b.val + carry
            carry = 1 if val >= 10 else 0
            a.val = val % 10
            # 现在a的值就是两个节点相加后的和了
            # 之后再次递归计算a.next和b.next
            a.next = add(a.next, b.next, carry)
            return a
        return add(l1, l2, 0)
