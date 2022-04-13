class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        if t == "":
            return False

        j = 0
        for i in t:
            if(i == s[j]):
                j += 1

            if j == len(s):
                return True

        return False
