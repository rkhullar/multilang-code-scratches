# https://leetcode.com/problems/swap-nodes-in-pairs/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def iter_list(node: ListNode):
    curr = node
    while curr:
        yield curr.val
        curr = curr.next

def print_list(node: ListNode):
    s = (str(x) for x in iter_list(node))
    print(', '.join(s))

def swap(node: ListNode):
    a, b = node, node.next
    if b:
        c = b.next
        a.next = c
        b.next = a

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, count = head, 0
        while curr:
            print_list(head)
            if count % 2 == 0:
                print('swap at ', curr.val)
                swap(curr)
            count += 1
            curr = curr.next
