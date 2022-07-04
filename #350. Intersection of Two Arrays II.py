class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        d2 = {}
        result = []

        for i in nums1:
            if(i in d1):
                d1[i] = d1[i]+1
            else:
                d1[i] = 1

        for i in nums2:
            if(i in d2):
                d2[i] = d2[i]+1
            else:
                d2[i] = 1
        print(d1, d2)
        for j in d1:
            if(j in d2):
                for k in range(min(d2[j], d1[j])):
                    result.append(j)

        return result
