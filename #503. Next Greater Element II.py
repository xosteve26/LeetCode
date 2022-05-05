class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l = []
        flag = False
        for i in range(len(nums)):
            flag = False
            for j in nums[i:]+nums[0:i]:
                if j > nums[i]:
                    l.append(j)
                    flag = True
                    break

            if not flag:
                l.append(-1)

        return l
