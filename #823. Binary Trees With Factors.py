class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        MOD=10**9 + 7

        dp={num:1 for num in arr}
        
        for i in range(len(arr)):
            for j in range(i):
                if(arr[i] % arr[j] == 0):
                    right=arr[i] // arr[j]
                    if right in dp:
                        dp[arr[i]]+=dp[arr[j]]*dp[right]
   
        return sum(dp.values())%MOD