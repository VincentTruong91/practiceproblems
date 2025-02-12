#O(n) time
#O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0

        while (r <= len(nums) - 1):
            if prices[l] >= prices[r]:
                continue #no profit (or negative profit)
            else: #there's positive profit
                currentProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, currentProfit)
                l = r
            r += 1 #regardless of profit or none
        return maxProfit