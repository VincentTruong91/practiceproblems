class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0

        while (r < len(prices)):
            if prices[l] < prices[r]:
                #this means that there is profit
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                #there's no profit or negative profit
                l = r
            
            r += 1

        return res
    
#time complexity -> O(n) because i'm using a while loop to itterate thorugh the prices
#space complexity -> O(1) due to not using any arrays for storing values or DS