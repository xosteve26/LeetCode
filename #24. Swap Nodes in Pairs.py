# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        curr = head
        nXt = curr.next
        newHead = nXt
        if not head.next.next:
            curr.next = nXt.next
            nXt.next = curr
            return newHead

        while curr and curr.next:
            #Swap Nodes
            curr.next = nXt.next
            nXt.next = curr

            #Establish Links Between Segments of swaps
            if prev:
                prev.next = nXt

            #Configure Pointers
            prev = curr
            curr = curr.next

            if curr:
                nXt = curr.next

        return newHead
