from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or k <= 0:
            return []

        fCount = Counter(words)
        heap = [(-freq, word) for word, freq in fCount.items()]
        heapq.heapify(heap)
        print(heap)

        result = [heapq.heappop(heap)[1] for _ in range(k)]

        return result
