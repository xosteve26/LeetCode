class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        d = {}
        sCount = {}
        for i in range(len(p)):
            d[p[i]] = 1+d.get(p[i], 0)
            sCount[s[i]] = 1+sCount.get(s[i], 0)

        res = [0] if sCount == d else []
        l = 0

        for r in range(len(p), len(s)):
            sCount[s[r]] = 1+sCount.get(s[r], 0)
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1

            if sCount == d:
                res.append(l)

        return res
