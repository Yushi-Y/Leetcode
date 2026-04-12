class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # only track min price so far, calculate profit each day
        # update max profit if higher than current profit
        # TC O(n), SC O(1)
        min_price = float('inf')
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            profit = p - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit

        # # difference array - TC O(n), SC O(n)
        # diff = [prices[i+1] - prices[i] for i in range(len(prices)-1)]
        # curr = max_sum = 0
        # for d in diff:
        #     curr = max(0, curr + d) # profit can not be lower than zerp
        #     max_sum = max(max_sum, curr)

        # return max_sum






        