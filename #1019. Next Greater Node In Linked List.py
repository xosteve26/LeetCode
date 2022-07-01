class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        current = head
        l = []
        stack = []
        while current:
            l.append(current.val)
            current = current.next

        result = [0]*len(l)
        for i in range(len(l)):
            while(stack and l[stack[-1]] < l[i]):
                curr = stack.pop()
                result[curr] = l[i]

            stack.append(i)
        return result
