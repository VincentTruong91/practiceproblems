#monotonic decreasing stack (always decreasing)
#time complexity -> O(n)
#space complexity -> O(n)
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #pair-list: [temp, index]
        result = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: #stack[-1] = top, [0] means temp
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = (index - stackIndex)
            stack.append([temp, index])
        return result
    