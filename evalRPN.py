#stack
#time complexity -> O(n) because uses for loop to itterate n elements in List
#space complexity -> O(n) because uses stack as data structure
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens :
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(token))
        return stack[0]