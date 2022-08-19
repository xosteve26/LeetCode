class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if(not nums or len(nums) < 3):
            return False
        FM = Counter(nums)
        HM = defaultdict(int)

        for num in nums:
            if(FM[num] == 0):
                continue

            if(HM[num] > 0):
                HM[num] -= 1
                HM[num+1] += 1

            elif(FM[num] > 0 and FM[num+1] > 0 and FM[num+2] > 0):
                FM[num+1] -= 1
                FM[num+2] -= 1

                HM[num+3] += 1
            else:
                return False

            FM[num] -= 1

        return True
