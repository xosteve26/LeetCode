class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        horizontalCuts.extend([0, h])
        verticalCuts.extend([0, w])
        horizontalCuts.sort(reverse=True)
        verticalCuts.sort(reverse=True)
        hans = []
        vans = []
        for i in range(len(horizontalCuts)-1):
            hans.append(horizontalCuts[i]-horizontalCuts[i+1])
        for i in range(len(verticalCuts)-1):
            vans.append(verticalCuts[i]-verticalCuts[i+1])
        return (max(hans)*max(vans)) % ((10**9)+7)
