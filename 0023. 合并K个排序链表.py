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

# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
# ``` python
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# ```
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# +
# my solution 1, crude loop soluble method, timeout
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = dummy = ListNode(None)

        index = 0
        while index < len(lists):
            if not lists[index]:
                lists.pop(index)
            else:
                index += 1

        while lists:
            min_index = 0
            for i, j in enumerate(lists):
                min_index = min(
                    min_index, i, key=lambda index: lists[index].val)
            result.next = lists[min_index]
            result = result.next
            lists[min_index] = lists[min_index].next
            if lists[min_index] == None:
                lists.pop(min_index)

        return dummy.next

# +
# my solution 2, crude loop soluble method, timeout
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def get_place(node, start, end):
            if start >= end:
                return start
            if lists[(start+end)//2].val < node.val:
                return get_place(node, (start+end)//2+1, end)
            elif lists[(start+end)//2].val > node.val:
                return get_place(node, start, (start+end)//2)
            else:
                return (start+end)//2

        result = dummy = ListNode(None)

        lists.sort(key=lambda node: float('inf') if not node else node.val)
        while lists and not lists[len(lists) - 1]:  # get rid of the None node
            lists.pop()

        while lists:
            s = lists.pop(0)
            result.next = s
            result = result.next
            if s.next:
                lists.insert(get_place(s.next, 0, len(lists)), s.next)
        return dummy.next


# +
_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/merge-k-sorted-lists/
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Maintain a min heap of tuples of (val, list index) for the next node in each list.
# Also maintain a list of the next node to be merged for each list index.
# Time - O(n log k) for n total nodes, each of which is pushed and popped from heap in log k time.
# Space - O(k) for heap of k nodes

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        prev = dummy = ListNode(None)
        next_nodes, heap = [], []

        for i, node in enumerate(lists):
            next_nodes.append(node)         # next_nodes[i] is the next node to be merged from lists[i]
            if node:
                heap.append((node.val, i))
        heapq.heapify(heap)

        while heap:
            value, i = heapq.heappop(heap)
            node = next_nodes[i]
            prev.next = node                # add node to merged list
            prev = prev.next
            if node.next:
                next_nodes[i] = node.next
                heapq.heappush(heap, (node.next.val, i))

        return dummy.next


# +
lists = [2, 4]


def get_place(node, start, end):
    if start == end:
        return start
    mid = (start+end)//2
    if lists[mid] < node:
        return get_place(node, mid+1, end)
    elif lists[mid] > node:
        return get_place(node, start, mid)
    else:
        return mid


print(get_place(5, 0, len(lists)))
