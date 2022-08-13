class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        d = {}
        for i in words:
            d[i] = 1 + d.get(i, 0)

        res = []
        wC = len(words)
        wL = len(words[0])

        for i in range(0, len(s)-(wC*wL)+1):
            seen = {}
            for j in range(wC):
                nextIndexOfWord = i+j*wL
                nextWord = s[nextIndexOfWord:nextIndexOfWord+wL]

                if (not nextWord in d):
                    break

                seen[nextWord] = 1 + seen.get(nextWord, 0)

                if (seen[nextWord] > d[nextWord]):
                    break

                if j+1 == wC:
                    res.append(i)

        return res
