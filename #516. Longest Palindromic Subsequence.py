class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1 = s
        text2 = s[::-1]
        #Raw Recursion - TC: O(2^N * 2^M)
        # def recursion(i1,i2):
        #     if i1<0 or i2<0:
        #         return 0
        #     #If there is a matching element at the present index
        #     if text1[i1]==text2[i2]:
        #         return 1+recursion(i1-1,i2-1)
        #     #If there isn't a matching index at he current index
        #     return 0+max(recursion(i1-1,i2), recursion(i1,i2-1))

        # return recursion(len(text1)-1,len(text2)-1)

        #Recursion with memoization - TC: O(N*M)
        # memo={}
        # def memoization(i1,i2):
        #     if (i1,i2) in memo:
        #         return memo[(i1,i2)]
        #     if i1<0 or i2<0:
        #         return 0
        #     #If there is a matching element at the present index
        #     if text1[i1]==text2[i2]:
        #         memo[(i1,i2)]=1+memoization(i1-1,i2-1)
        #         return memo[(i1,i2)]
        #     #If there isn't a matching index at the current index
        #     memo[(i1,i2)]=0+max(memoization(i1-1,i2), memoization(i1,i2-1))
        #     return memo[(i1,i2)]

        # return memoization(len(text1)-1,len(text2)-1)

        #2D Dynamic Programming Solution
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = 0+max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
