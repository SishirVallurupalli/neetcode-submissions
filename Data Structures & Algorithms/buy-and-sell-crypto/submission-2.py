class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        L = 0
        R = 1
        while R < len(prices):
            if prices[L] > prices[R]:
                L = R
                R += 1
            else:
                maxProfit = max(maxProfit, prices[R] - prices[L])
                R += 1
        return maxProfit
