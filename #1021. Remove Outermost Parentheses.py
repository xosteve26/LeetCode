class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        index = []
        for i in range(len(s)):
            if(not stack):
                stack.append(s[i])
                index.append(i)
                continue
            if(s[i] == ')' and stack[-1] == '('):
                stack.pop()
                if not stack:
                    index.append(i)
                continue
            else:
                stack.append(s[i])

        result = ""
        for j in range(len(s)):
            if j not in index:
                result += s[j]

        return result
