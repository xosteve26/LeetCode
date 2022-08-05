class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def helper(i, l, target):
            if target == 0:
                res.append(l[:])
                return

            if target < 0 or i >= len(candidates):
                return

            l.append(candidates[i])
            helper(i+1, l, target-candidates[i])
            l.pop()
            curr = candidates[i]

            while i < len(candidates) and candidates[i] == curr:
                i = i+1

            helper(i, l, target)

        res = []
        helper(0, [], target)
        return res
