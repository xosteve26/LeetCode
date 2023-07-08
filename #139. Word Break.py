class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #TC: O(M^N) N = length of string
        # def backtrack(i):
        #     if i>=len(s): return True

        #     for word in wordDict:
        #         if(word == s[i:i+len(word)]):
        #             if backtrack(i+len(word)): return True

        #     return False

        # return backtrack(0)

        #TC: O(N*M*K) m=length of dict, k=length of each substring in if
        dp = [False ] * (len(s)+1)
        dp[len(s)] = True
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if(s[i:i + len(word)] == word and dp[i+len(word)]):
                    dp[i] = True
                if dp[i]: break

        return dp[0]