class Solution:
    def checkValidString(self, s: str) -> bool:
        stack, starStack = [], []

        #Iterate through every element in "s"
        for i in range(len(s)):
            bracket = s[i]
            #In case of a opening parenthesis exists, append it into a stack, so that lator on if a closing parenthesis or a star exists we can close it.
            if bracket == "(":
                stack.append(i)

            #In case of a closing parenthesis, we can only close an opening parenthesis if:
            #- it exists in the "stack" i.e an opening parenthesis
            #- if a star exists in the starStack such that the star can be transformed to an opening parenthesis and then closed.
            #- else we must return False because there isn't anything to close with the current bracket.
            elif bracket == ")":
                if stack:
                    stack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False

            #In case of a star we just append it to the starStack
            else:
                starStack.append(i)

        #In the end of the for loop is there isn't anything in the stack then it means all the opening parentehsis has been closed so we can return True and it doesnt matter if there are remaining *s in the starStack cuz they can by default be nuls.
        if not stack:
            return True

        #However if there are elements in the stack and nothing in the starStack then we have to return False because we cannot transform anything into a closing parenthesis to close down our remaining opening parenthesis.
        if not starStack:
            return False

        #In case where we have elements in the stack and starStack then we can start popping stars from the starStack and consider them as closing parenthesis so that we can close down our opening parenthesis. However we can do this only if the star index is after the opening parenthesis index.
        while starStack and stack:
            openingParenthesisIndex = stack.pop()
            starIndex = starStack.pop()

            if starIndex < openingParenthesisIndex:
                return False
        #In the them if the stack is empty then we can return True else False because if means we did not have enough stars to close down all our opening parenthesis.
        return True if not stack else False
