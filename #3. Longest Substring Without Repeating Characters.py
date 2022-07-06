class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lSubstring = 0
        l = 0
        r = 0
        u = set()

        while r < len(s):
            while(s[r] in u):
                u.remove(s[l])
                l += 1

            u.add(s[r])
            lSubstring = max(lSubstring, r-l+1)
            r += 1

        return lSubstring
