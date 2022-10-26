# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        end = head
        length = 0
        while end:
            length += 1
            end = end.next

        curr = head

        dummy = pre_left = pre_right = ListNode(0, head)
        l = r = head
        c = 1
        while curr:

            if c == k-1:
                pre_left = curr
                l = pre_left.next

            if c == length-k:
                pre_right = curr
                r = pre_right.next
            c += 1
            curr = curr.next
        if l == r:
            return head

        pre_left.next, pre_right.next = r, l
        l.next, r.next = r.next, l.next

        return dummy.next
