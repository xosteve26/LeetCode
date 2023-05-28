import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # TC O(max(piles) * N) // N= length of piles
        # piles.sort()
        # for r in range(1, piles[-1] + 1):
        #     NO_OF_HOURS = 0
        #     for pile in piles:
        #         NO_OF_HOURS += math.ceil(pile/r)
        #         if NO_OF_HOURS > h:
        #             break
        #     if NO_OF_HOURS <= h:
        #         return r

        # TC: O(log(max(piles)) * N) // N = length of piles
        START, END = 1, max(piles)
        MINIMUM = float("inf")
        while START<=END:
            k = (START + END) // 2
            noOfHours=0
            for pile in piles:
                noOfHours+=math.ceil(pile/k)

            if noOfHours<=h:
                MINIMUM = min(MINIMUM, k)
                END = k - 1
            else:
                START = k + 1

        return MINIMUM
