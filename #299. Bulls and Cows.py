class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cows, bulls = 0, 0
        s, g = list(secret), list(guess)
        i, j = 0, 0

        while j < len(secret):
            if(s[i] == g[i]):
                bulls += 1
                s.pop(i)
                g.pop(i)
            else:
                i += 1
            j += 1

        x = Counter(s)
        for val in g:
            if(val in x and x[val] > 0):
                x[val] -= 1
                cows += 1

        return str(bulls)+'A'+str(cows)+'B'
