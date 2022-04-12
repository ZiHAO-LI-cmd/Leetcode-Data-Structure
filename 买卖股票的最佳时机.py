class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        dp = [0] * len(prices)
        minPrice = prices[0]

        # dp[i] 表示前 i 天中的最大利润
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minPrice)
        return dp[-1]
        