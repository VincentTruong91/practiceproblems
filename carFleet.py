#stack
#time complexity -> O(nlogn) due to using the sorted algorithm + forloop
#space complexity -> O(n) memory due to using stack
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        #create an array of pairs

        stack = []
        for p,s in sorted(pair)[::-1]: #reverse sorted order
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]: #if we have 2 cars in stack
            #and car at top of stack is going faster than car in front of it
                stack.pop()
        return len(stack)