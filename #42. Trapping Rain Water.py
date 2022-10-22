class Solution:
    def trap(self, height: List[int]) -> int:
        #Find the max left value for each element
        maxLeft = [0]*len(height)
        maxL = 0
        for i, l in enumerate(height):
            maxLeft[i] = maxL
            maxL = max(maxL, l)

        #Find the max right value for each element in the list
        maxRight = [0]*len(height)
        maxR = 0
        for r in range(len(height)-1, -1, -1):
            maxRight[r] = maxR
            maxR = max(maxR, height[r])

        #Compute the min of max R & L for each iteration of height  and subtract it from height to obtain the amount of water that can be trapped at each iteration.
        result = 0
        for j in range(len(height)):
            compute = min(maxRight[j], maxLeft[j])-height[j]
            result += compute if compute > 0 else 0

        return result
