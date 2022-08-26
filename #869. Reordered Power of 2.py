from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        c = Counter(str(n))
        N, i = 0, 0

        while N < 10**9:
            N = 2**i
            d = Counter(str(N))
            if c == d:
                return True
            i += 1
        return False
