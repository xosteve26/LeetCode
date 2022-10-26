# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = ListNode(float("-inf"), None)
        dup = set()
        while curr:
            if curr.val == prev.val:
                dup.add(curr.val)
                prev.next = prev.next.next
                curr = curr.next
                continue

            prev = curr
            curr = curr.next

        newCurr = head
        dummy = newPrev = ListNode(0, head)
        while newCurr:
            if newCurr.val in dup:
                newPrev.next = newPrev.next.next
                newCurr = newCurr.next
                continue

            newPrev = newCurr
            newCurr = newCurr.next

        return dummy.next
