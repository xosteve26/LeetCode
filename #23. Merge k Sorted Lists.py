# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = []

        for linkedList in lists:
            node = linkedList
            while node:
                heapq.heappush(heap, node.val)
                node = node.next

        LINKEDLIST = dummy = ListNode(0)
        while heap:
            item = heapq.heappop(heap)
            dummy.next = ListNode(item)
            dummy = dummy.next

        return LINKEDLIST.next
