class Solution:
    def containerWithMostWater(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0

        while (l < r):
            width = r - l
            height = min(heights[l], heights[r])

            currentArea = width * height

            res = max(res, currentArea)

        return res
    
#time complexity -> O(n) while using a while loop
#space complexity -> O(1) becuase we only need the pointers and no data structure used

