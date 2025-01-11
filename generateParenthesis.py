#Stack and Recursion
#Time complexity -> O(4^n / sqrt(n)) using Catalan because of recursion
#space complexity -> O(n) because we used stack
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        #example run: [((()))], [(())()]
        #stack = [(] numOfOpen = 1, numOfClosed = 0
        #stack = [((] numOfOpen = 2, numOfClosed = 0
        #stack = [(((] numOfOpen = 3, numOfClosed = 0
        #stack = [((()] numOfOpen = 3, numOfClosed = 1
        #stack = [((())] numOfOopen = 3, numOfClosed = 2
        #stack = [((()))] numOfOpen = 3, numOfClosed = 3
        #stack = [((())], [((()], [(((], [((], ----> [(()], [(())], [(())(], [(())()]


        #we want to use recursion
        def backtracking(numOfOpen : int, numOfClosed : int):
            if numOfOpen == numOfClosed == n:
                result.append("".join(stack))
                return
            
            if numOfOpen < n:
                stack.append("(")
                backtracking(numOfOpen + 1, numOfClosed)
                stack.pop() # we pop because we aren't passing it down with backtracking, it's a global varaible isntead
                #and also, pop to maintain the correct state of the stack for susequent calls
                #when done exploring a particular path for the current level, pop
                #without pop, stack would accumulate all parenthesis for all recursive calls
            
            if numOfClosed < numOfOpen:
                stack.append(")")
                backtracking(numOfOpen, numOfClosed + 1)
                stack.pop()
                    
        backtracking(0,0)
        return result