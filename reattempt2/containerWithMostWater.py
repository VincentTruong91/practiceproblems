class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxAreaFound = 0

        while l < r:
            height = max(heights[l], heights[r])
            width = r - l

            currentArea = height * width

            maxAreaFound = max(maxAreaFound, currentArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxAreaFound

#two pointers
#time complexity -> O(n) goes through each item in list of size n
#space complexity -> O(1) no list or DS used.