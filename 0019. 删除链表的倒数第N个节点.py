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

# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
# ```
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
# ```
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# +
# my solution 1, in two pass
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        newhead = pointer = ListNode(None)
        pointer.next = head
        length = 0
        index = 0
        
        while pointer.next:
            pointer = pointer.next
            length += 1
        
        pointer = newhead
        for i in range(length - n):
            pointer = pointer.next
        
        temp = pointer.next
        pointer.next = pointer.next.next
#         del temp
        
        return newhead.next

# +
# my solution 2, in one pass


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None

        nodes = list()
        pointer = ListNode(None)
        pointer.next = head

        while pointer:
            nodes.append(pointer)
            pointer = pointer.next
        
        nodes[len(nodes)-1-n].next = nodes[len(nodes)-1-n].next.next
#         del nodes[len(nodes)-n]
        return nodes[0].next


# +
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Given a linked list, remove the nth node from the end of list and return its head.

# Advance first pointer n steps then advance both pointers at same rate.
# Time - O(n)
# Space - O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first, second = head, head

        for i in range(n):      # move first n steps forwards
            first = first.next
        if not first:
            return head.next

        while first.next:       # move both pointers until first is at end
            first = first.next
            second = second.next
        second.next = second.next.next  # nth from end is second.next
        return head
