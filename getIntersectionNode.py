# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        c = headA
        while c:
            s.add(c)
            c = c.next
        c = headB
        while c:
            if c in s:
                return c
            c = c.next
        return None
