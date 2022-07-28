class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        c = Counter(s)

        for i in t:
            if i in c:
                c[i] -= 1
                if c[i] == 0:
                    c.pop(i)
            else:
                return False

        return True if not c else False
