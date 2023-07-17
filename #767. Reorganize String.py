class Solution:
    def reorganizeString(self, s: str) -> str:
        x = Counter(s)

        heap = []

        for k,v in x.items():
            heapq.heappush(heap, [-v, k])

        prev = None
        res=""
        while heap or prev:
            if not heap and prev:
                return ""

            freq, c = heapq.heappop(heap)
            res+=c
            freq+=1

            if prev:
                heapq.heappush(heap, prev)
                prev=None

            if freq!=0: prev = [freq, c]

        return res