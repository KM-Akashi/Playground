# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        a = head
        if a.next is None:
            return a
        b = head.next
        if b.next is None:
            a.next = None
            b.next = a
            return b
        c = b.next

        a.next = None
        while c is not None:
            b.next = a
            a = b
            b = c
            c = c.next
        b.next = a
        return b
