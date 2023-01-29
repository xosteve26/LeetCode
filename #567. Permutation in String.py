class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #O(26*N) time and O(26) space
        if len(s2) < len(s1):
            return False

        LENGTH = len(s1)

        s1Count = [0 for _ in range(26)]
        for CHAR in s1:
            s1Count[ord(CHAR) % 97] += 1

        s2RunningCounter = [0 for _ in range(26)]
        for i in range(LENGTH):
            s2Char = s2[i]
            s2RunningCounter[ord(s2Char) % 97] += 1

        l, r = 0, LENGTH-1
        while l <= r and r < len(s2):
            if s2RunningCounter == s1Count:
                return True
            s2RunningCounter[ord(s2[l]) % 97] -= 1
            l += 1
            r += 1
            if r < len(s2):
                s2RunningCounter[ord(s2[r]) % 97] += 1

        return False

        # counts=Counter(s1)
        # variableCounts=counts.copy()
        # l,r=0,0

        # while l<=r and r<len(s2):
        #     CHARACTER=s2[r]

        #     if CHARACTER in variableCounts:
        #         variableCounts[CHARACTER]-=1
        #         if not variableCounts[CHARACTER]:
        #             variableCounts.pop(CHARACTER)
        #         if not variableCounts:
        #             return True
        #         r+=1
        #     else:
        #         variableCounts=counts.copy()
        #         l+=1
        #         r=l

        # return False
