class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for character in word:
            curr = curr.children[character]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for character in word:
            if character not in curr.children:
                return False
            curr = curr.children[character]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for character in prefix:
            if character not in curr.children:
                return False
            curr = curr.children[character]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
