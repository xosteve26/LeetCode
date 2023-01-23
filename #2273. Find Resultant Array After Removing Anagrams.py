class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        prev = [words[0], []]
        countOfChars = [0 for _ in range(26)]
        for c in words[0]:
            countOfChars[ord(c) % 97] += 1
        prev[1] = countOfChars

        i = 1
        while i < len(words):
            countOfChars = [0 for _ in range(26)]
            word = words[i]
            print(word, prev)
            for c in word:
                countOfChars[ord(c) % 97] += 1

            if countOfChars == prev[1]:
                words.pop(i)
                continue
            prev[0] = words[i]
            prev[1] = countOfChars
            i += 1
        return words
