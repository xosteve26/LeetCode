class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        a = ''
        for i in num:
            a += str(i)
        a = int(a)+k
        return list(str(a))
