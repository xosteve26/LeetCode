# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        if length == 1 or length == 0:
            return None

        goal = length//2
        prev = None
        newCurr = head
        start = head
        while newCurr:
            if goal == 0:
                prev.next = prev.next.next
                return start

            goal -= 1
            prev = newCurr
            newCurr = newCurr.next
