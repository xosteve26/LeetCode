from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = dict(Counter(arr))
        vals = sorted(c.values(), key=lambda x: -x)

        total = 0

        for i, j in enumerate(vals):
            total += j

            if(total >= len(arr)//2):
                return i+1
