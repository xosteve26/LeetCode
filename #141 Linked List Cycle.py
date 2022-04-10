class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        if head == None:
            return False
        while current.next:
            if(current.next.val == 'cycle'):
                return True
            current.val = "cycle"
            current = current.next

        return False
