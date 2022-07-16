class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        for i in range(len(s)):
            if s[i] not in d1 or d1[s[i]] == t[i]:
                d1[s[i]] = t[i]
            else:
                return False

        for i in range(len(s)):
            if t[i] not in d2 or d2[t[i]] == s[i]:
                d2[t[i]] = s[i]
            else:
                return False

        return True
