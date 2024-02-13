"""
https://leetcode.com/problems/swap-nodes-in-pairs
https://youtu.be/o811TZLAWOo
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(val=None, next=head)
        prev, curr = start, head
        while curr and curr.next:
            a, b = curr, curr.next
            c = b.next
            # reverse
            b.next = a
            a.next = c
            prev.next = b
            # iterate
            prev, curr = a, c
        return start.next
