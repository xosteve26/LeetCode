# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        curr = head
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next

        nCur = head
        while stack and nCur:
            value = stack.pop()
            if value != nCur.val:
                return False
            nCur = nCur.next

        return True