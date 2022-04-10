class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if head == None:
            return None
        while current.next:
            if(current.next.val == 'cycle'):
                return current.next
            current.val = 'cycle'
            current = current.next
        return None
