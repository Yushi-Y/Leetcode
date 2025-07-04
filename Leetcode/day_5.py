# Best Time to Buy and Sell Stock I
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
           return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit


# Best Time to Buy and Sell Stock II 
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


# Longest Palindrome
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0

        # Create a frequecy dictionary of character counts
        freq = {}
        for char in s:
            # Get the count for each character
            freq[char] = freq.get(char, 0) + 1

        has_odd_freq = False
        length = 0

        for char_freq in freq.values():
            if char_freq % 2 == 0:
                length += char_freq
            else:
                # Extract the floor even number from the odd freq
                length += char_freq - 1
                has_odd_freq = True
        
        # Add 1 to the length if there is a single character left to be put in the middle
        return length + has_odd_freq
