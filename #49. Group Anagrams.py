class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultDict = defaultdict(list)
        for word in strs:
            charCount = [0 for _ in range(26)]
            for CHAR in word:
                charCount[ord(CHAR) % 97] += 1
            resultDict[tuple(charCount)].append(word)

        return resultDict.values()
