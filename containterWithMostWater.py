#two pointer
#time complexity -> O(n) using a while loop
#space complexity -> O(1) not using any data structure besides using pointers
class Solution:
    def containerWithMostWater(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0 #gives us the most amount of water

        while l < r:
            heightOfContainer = min(heights[l], heights[r])
            widthOfContainer = r - l
            waterOfContainer = heightOfContainer * widthOfContainer

            res = max(res, waterOfContainer)
            if l <= r:
                l += 1
            else: #r > l
                r += 1
            
        return res