class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, current = None, head
        prevNode, nextNode = dummy, None
        leftNode, rightNode = None, None

        if(left == right):
            return head
        current = head
        for i in range(left-1):
            prevNode, current = current, current.next

        leftNode = current
        current = leftNode

        prev = None
        for i in range(right-left+1):
            nXt = current.next
            current.next = prev
            prev = current
            current = nXt

        rightNode = prev
        nextNode = current

        prevNode.next = rightNode
        leftNode.next = nextNode
        return dummy.next
