class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        max_profit = 0
        diff = 0 
        n = len(prices)
        for i in range (1,n):
            diff = prices[i] - prices[i-1]
            profit = profit + diff
            max_profit = max(max_profit , profit)
            if profit<0:
                profit = 0 
        return (max_profit)
        