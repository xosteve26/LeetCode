class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #Create a dictionary to map the pattern to the words
        charToWord = {}
        #Create a dictionary to map the words to the pattern
        wordToChar = {}
        #Split the string into a list of words
        words = s.split()
        LENGTH = len(words)
        #If the length of the pattern is not equal to the length of the list of words, return False
        if len(pattern)!=LENGTH:
            return False

        #Iterate through the pattern and the list of words
        for i in range(LENGTH):
            #If the pattern character is already in the dictionary and the word associated to that pattern character is not equal to the word in the dictionary, return False
            if pattern[i] in charToWord and charToWord[pattern[i]] != words[i]:
                return False
            #If the word is already in the dictionary and the word is not equal to the pattern character in the dictionary, return False
            if words[i] in wordToChar and wordToChar[words[i]] != pattern[i]:
                return False
            #If the pattern character is not in the dictionary, add it to the dictionary and map it to the word
            charToWord[pattern[i]] = words[i]
            #If the word is not in the dictionary, add it to the dictionary and map it to the pattern character
            wordToChar[words[i]] = pattern[i]
        
        return True
