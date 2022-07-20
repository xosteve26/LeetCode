class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def helper(I, target, lst):
            if target == 0:
                res.append(lst[:])
                return

            if target < 0:
                return

            if(I < len(candidates)):
                lst.append(candidates[I])
                helper(I, target-candidates[I], lst)
                lst.pop()
                helper(I+1, target, lst)

        res = []
        helper(0, target, [])
        return res
