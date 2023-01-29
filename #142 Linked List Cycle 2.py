# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow, fast = head, head
        isCyclic = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                isCyclic = True
                break

        if not isCyclic:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast
