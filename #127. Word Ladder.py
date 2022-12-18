class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        queue = deque()
        queue.append((beginWord, 1))
        lst = set(wordList)

        if endWord not in lst:
            return 0

        seen = set()
        seen.add(beginWord)

        while queue:
            for i in range(len(queue)):
                word, seq = queue.popleft()
                original_word = word[:]

                if word == endWord:
                    return seq

                for c in range(len(word)):
                    for ch in range(97, 123):
                        word = word[:c]+chr(ch)+word[c+1:]
                        if word in lst and word not in seen:
                            queue.append((word, seq+1))
                            seen.add(word)

                    word = original_word
        return 0
