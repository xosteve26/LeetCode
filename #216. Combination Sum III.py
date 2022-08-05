class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(10)]

        def helper(i, l, target):
            if(target == 0 and len(l) == k):
                res.append(l[:])
                return

            if target < 0 or i > 9 or len(l) > k:
                return

            l.append(candidates[i])
            helper(i+1, l, target-candidates[i])
            l.pop()
            helper(i+1, l, target)

        res = []
        helper(1, [], n)
        return res
