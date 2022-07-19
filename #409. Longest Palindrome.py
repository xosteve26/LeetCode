class Solution:
    def longestPalindrome(self, s: str) -> int:
        x = Counter(s)
        if len(x) == 1:
            return len(s)
        odd = 0
        result = 0
        for i in x.values():
            if i > 1:
                if i % 2 == 0:
                    result += i
                else:
                    result += i-1
                    odd += 1
            else:
                odd += 1

        if odd > 0:
            result += 1
        return result
