# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 0

        while current:
            count += 1
            current = current.next

        middle = head
        print(int(count/2))
        for i in range(int(count/2)):
            middle = middle.next

        return middle
