class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freq = [[] for y in range(len(nums)+1)]
        for i in nums:
            d[i] = 1+d.get(i, 0)

        res = []
        for key, val in d.items():
            freq[val].append(key)

        c = k
        for q in range(len(freq)-1, 0, -1):
            for w in freq[q]:
                res.append(w)
                c -= 1
                if c == 0:
                    return res
