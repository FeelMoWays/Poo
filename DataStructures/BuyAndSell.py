class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minn = prices[0]
        maxx = 0
        for i in range(1,len(prices)):
            minn = min(minn,prices[i])
            maxx = max(maxx,prices[i] - minn)
        return maxx