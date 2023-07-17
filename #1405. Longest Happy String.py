import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        heap = []

        if(a>0): heapq.heappush(heap, (-a, "a"))
        if(b>0): heapq.heappush(heap, (-b, "b"))
        if(c>0): heapq.heappush(heap, (-c, "c"))

        res = ""

        while heap :
            freq, chr = heapq.heappop(heap)
            if len(res)>=2 and res[-1] == res[-2] == chr:
                if not heap: return res
                notRepeatingCharsFreq,  notRepeatingChar = heapq.heappop(heap)
                res+=notRepeatingChar
                notRepeatingCharsFreq+=1

                if notRepeatingCharsFreq!=0:
                    heapq.heappush(heap, (notRepeatingCharsFreq, notRepeatingChar))
            else:
                res+=chr
                freq+=1

            if freq!=0: heapq.heappush(heap, (freq, chr))

        return res