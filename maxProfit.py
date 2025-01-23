#sliding window (with 2 pointer)
#time complexity -> O(n)
#space complexity -> O(1)
class Solution:
    def maxProfit(self, profits : List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0

        while r < len(profits):
            #if current value from pointers can make a profit
            if profits[l] < profits[r]:
                profit = profits[r] - profits[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1 #right pointer increment regardless of profit/noprofit
        return maxProfit


