class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pre = newHead = ListNode(None)
        pre.next = head
        cur = pre
        while cur:
            nex = cur.next
            if cur.val == val:
                pre.next = nex
            else:
                pre = cur
            cur = nex
        
        return newHead.next
    
