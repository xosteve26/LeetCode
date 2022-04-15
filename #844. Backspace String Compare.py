class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack, tStack = [], []

        for i in s:
            if i == '#':
                if sStack:
                    sStack.pop()
            else:
                sStack.append(i)

        for j in t:
            if j == '#':
                if tStack:
                    tStack.pop()
            else:
                tStack.append(j)

        return True if sStack == tStack else False
