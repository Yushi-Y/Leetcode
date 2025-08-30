# (Medium) Best Time to Buy and Sell Stock II 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Intuition: 
        # If tomorrow's price is higher than today's, buy today and sell tomorrow. 
        # Repeat for every such pair, which effectively captures all upward trends.
        if len(prices) == 1:
            return 0
        
        total_profit = 0
        for i in range(1, len(prices)): 
            if prices[i] - prices[i-1] > 0:
                total_profit += prices[i] - prices[i-1]

        return total_profit


