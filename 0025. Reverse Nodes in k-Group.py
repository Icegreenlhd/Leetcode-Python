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

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
# ```
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
# ```
# Note:
#
# - Only constant extra memory is allowed.
# - You may not alter the values in the list's nodes, only nodes itself may be changed.

# +
# my solution 1
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def check_num(head, k):
            for _ in range(k):
                if not head:
                    return False
                head = head.next
            return True
        
        assert k > 0, "k is greater "
        assert check_num(head, k), "k is greater than the size of the linked list"
        if k < 2: 
            return head
        
        result = dummy = ListNode(None)
        
        while head:
            if check_num(head, k):
                for _ in range(k):
                    tmp = head
                    head = head.next
                    tmp.next = result.next
                    result.next = tmp
                for _ in range(k):
                    result = result.next
            else:
                break
        result.next = head
        return dummy.next
        


# +
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# You may not alter the values in the nodes, only nodes itself may be changed.
# Only constant memory is allowed.

# If there are at least k nodes, recursively reverse remainder and append reversed group to reversed remainder.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2:
            return head

        node = head
        for _ in range(k):
            if not node:
                return head     # return head if there are not at least k nodes
            node = node.next
        # else node is now head of second group

        # reverse remainder after this group
        prev = self.reverseKGroup(node, k)

        for _ in range(k):      # reverse this group, adding in front of prev
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
