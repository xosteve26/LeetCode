class Solution:
    def longestPalindrome(self, s: str) -> str:

        def recursion(even, longestSubstring, result):
            for j in range(len(s)):

                if not even:
                    l, r = j, j
                else:
                    l, r = j, j+1

                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if(r-l+1) > longestSubstring:
                        longestSubstring = r-l+1
                        result = s[l:r+1]

                    l -= 1
                    r += 1
            return result

        odd = recursion(False, 0, "")
        eve = recursion(True, 0, "")
        return odd if len(odd) > len(eve) else eve
