class Solution:
    def validParenthesis(self, s:str) -> bool:
        closedOpenPairs = {']': '[', '}' : '{', ')' : '('}
        stack = []

        for char in s:
            if char in closedOpenPairs: #closed pair
                if stack and stack[-1] == closedOpenPair[char]:
                    stack.pop()
                else:
                    return False

            else: #open char
                stack.append(char)

        if stack:
            return False
        else:
            return True