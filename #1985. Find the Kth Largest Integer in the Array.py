class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []

        for val in nums: heapq.heappush(heap, -int(val))

        KLargest = float("inf")

        while heap and k:
            KLargest = -(heapq.heappop(heap))
            k-=1

        return str(KLargest)
            