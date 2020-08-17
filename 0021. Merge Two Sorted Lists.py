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

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
# ```
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# ```

# +
# my solution 1
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        p = head = ListNode(None)
        while p1:
            if not p2:
                p.next = p1
                return head.next
            
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
                
            p = p.next
            
        if p2:
            p.next = p2
        return head.next


# +
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Whilst there are nodes in both lists, link to lowest head node and increment that list.  Finally link to
# the list with remaining nodes.
# Time - O(m+n)
# Space - O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):

        prev = dummy = ListNode(None)       # new dummy head for the merged list

        while l1 and l2:                    # link prev to the lowest node

            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        prev.next = l1 or l2                # link prev to the list with remaining nodes
        return dummy.next
