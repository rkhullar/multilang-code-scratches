# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        result = None
        while curr:
            a, b = curr, curr.next
            if b:
                print(a.val, b.val)
                t = b.next
                b.next = a
                a.next = t
                curr = t
                if not result:
                    result = b
            else:
                break
        return result

        # 1->2->3->4
        #  a,b = 1,2
        #  t = 3
        #  2.next = 1
        #  1.next = 3
        #  curr = 3
        # 2->1->3->4
        #  a,b = 3,4
        #  t = null
        #  4.next = 3
        #  3.next = null
        #  curr = null
        ## problem
        # 1.next != 4
