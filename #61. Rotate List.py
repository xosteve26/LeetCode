# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        #Get Length
        current = head
        length = 1
        while current.next:
            length += 1
            current = current.next

        tail = current
        k = k % length
        if k == 0:
            return head
        move = length-k
        nCurrent = head
        for i in range(move-1):
            nCurrent = nCurrent.next

        newHead = nCurrent.next

        nCurrent.next = None
        tail.next = head
        return newHead
