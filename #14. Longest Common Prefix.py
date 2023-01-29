class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestCommonPrefix = ""
        minWord, minLength = "", float("inf")
        for word in strs:
            if len(word) < minLength:
                minWord, minLength = word, len(word)

        for i in range(minLength):
            for word in strs:
                if word[i] != minWord[i]:
                    return longestCommonPrefix
            longestCommonPrefix += word[i]

        return longestCommonPrefix
