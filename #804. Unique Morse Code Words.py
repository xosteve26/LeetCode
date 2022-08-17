class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                      "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        s = set()

        def helper(words):
            if not words:
                return

            word = words.pop(0)
            transform = ''

            for i in word:
                transform += morse_code[ord(i) % 97]

            s.add(transform)

            helper(words)

        helper(words)
        return len(s)