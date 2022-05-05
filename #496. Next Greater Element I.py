class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                d[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        l = []
        for i in nums1:
            if i in d:
                l.append(d[i])
            else:
                l.append(-1)
        return l
