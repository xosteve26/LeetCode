class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowelsL = ['a', 'e', 'i', 'o', 'u']
        vowelsU = ['A', 'E', 'I', 'O', 'U']
        left, right = 0, len(s)-1
        while left < right:
            if((s[left] in vowelsL or s[left] in vowelsU) and (s[right] in vowelsL or s[right] in vowelsU)):
                s[left], s[right] = s[right], s[left]
                right -= 1
                left += 1
            elif(s[left] in vowelsL or s[left] in vowelsU):
                right -= 1
            elif(s[right] in vowelsL or s[right] in vowelsU):
                left += 1
            else:
                right -= 1
                left += 1

        return ''.join(s)
