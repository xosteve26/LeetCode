class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        t = pattern
        result = []
        for word in words:
            d1 = {}
            d2 = {}
            flag = True
            for i in range(len(word)):
                if word[i] not in d1 or d1[word[i]] == t[i]:
                    d1[word[i]] = t[i]
                else:
                    flag = False
                    break
            print("D!", d1)
            for i in range(len(word)):
                if t[i] not in d2 or d2[t[i]] == word[i]:
                    d2[t[i]] = word[i]
                else:
                    flag = False
                    break
            print("D@", d2)
            if(flag):
                result.append(word)
        return result
