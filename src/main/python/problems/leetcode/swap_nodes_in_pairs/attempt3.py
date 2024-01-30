# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections.abc import Iterator, Iterable


def iter_pairs(start: ListNode) -> Iterator[tuple[ListNode, ListNode]]:
    curr = start
    while curr:
        a, b = curr, curr.next
        yield a, b
        curr = b.next if b else None

def build_list(data: Iterable) -> ListNode:
    start, prev = None, None
    for item in data:
        node = ListNode(val=item)
        if not start:
            start = node
        if prev:
            prev.next = node
        prev = node
    return start

def iter_list(start: ListNode) -> Iterator[ListNode]:
    curr = start
    while curr:
        yield curr.val
        curr = curr.next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result, prev = None, None


        # pairs = list(iter_pairs(head))
        # for a, b in pairs:
        #     print(a.val, b.val if b else None)

        pairs = build_list(iter_pairs(head))
        # for pair in iter_list(pairs):
        #     a, b = pair
        #     print(a.val, b.val if b else None)

        for a, b in iter_list(pairs):
            print(a.val, b.val if b else None)
            if not result:
                result = b
            if b:
                b.next = a
            if prev:
                prev.next = b
            prev = a
        return result
