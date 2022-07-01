class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l = title.split()

        for i in range(len(l)):
            if(len(l[i]) == 1 or len(l[i]) == 2):
                l[i] = l[i].lower()

            else:
                l[i] = l[i][0].upper()+l[i][1:].lower()

        return ' '.join(l)
