class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        if len(s) == 2:
            if(s[1]+s[0] == goal):
                return True
            else:
                return False
        if s == goal and len(set(s)) != len(s):
            return True
        elif(s == goal and len(set(s)) == len(s)):
            return False

        d = []
        for i in range(len(s)):
            if(s[i] != goal[i]):
                d.append(i)

        if(len(d) == 2):
            if(s[:d[0]]+s[d[1]]+s[d[0]+1:d[1]]+s[d[0]]+s[d[1]+1:] == goal):
                return True
            else:
                return False
        else:
            return False
