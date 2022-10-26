# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = [0]
        sum2 = [0]

        s1 = l1
        while s1:
            sum1[0] = sum1[0]*10+s1.val
            s1 = s1.next

        s2 = l2
        while s2:
            sum2[0] = sum2[0]*10+s2.val
            s2 = s2.next

        total = str(sum1[0]+sum2[0])

        result_pointer = dummy = ListNode(0)

        for i in total:
            dummy.next = ListNode(i)
            dummy = dummy.next

        return result_pointer.next
