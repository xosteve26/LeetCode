class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        d = []
        for i in range(len(s1)):
            if(s1[i] != s2[i]):
                d.append(i)

        if(len(d) == 2):
            if(s1[:d[0]]+s1[d[1]]+s1[d[0]+1:d[1]]+s1[d[0]]+s1[d[1]+1:] == s2):
                return True
            else:
                return False
        else:
            return False
