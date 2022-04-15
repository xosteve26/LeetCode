class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack:
                if i == stack[-1]:
                    stack.pop()
                    continue
            stack.append(i)
        return ''.join(stack)
