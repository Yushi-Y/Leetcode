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
    # Logic: For each character count (for loop): 
    # If even, add full count. If odd, add count - 1 (largest even part). 
    # If an odd count was found, add an additional 1 to place a single odd letter in the center.

    def longestPalindrome(self, s: str) -> int:
        # Edge case
        if not s:
            return 0
        
        freq_dict = {}
        for char in s:
            freq_dict[char] = freq_dict.get(char, 0) + 1

        has_odd_freq = False
        length = 0

        for count in freq_dict.values():
            if count//2 == 0:
                length += count
            else:
                length += count-1
                has_odd_freq = True
        
        return length + has_odd_freq

# Or use Counters 
# from collections import Counter

# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         # Edge case
#         if not s:
#             return 0
        
#         counts = Counter(s) # Counter({'c': 4, 'd': 2, 'a': 1, 'b': 1})

#         has_odd_freq = False
#         length = 0

#         for count in counts.values():
#             if count//2 == 0:
#                 length += count
#             else:
#                 length += count-1
#                 has_odd_freq = True
        
#         return length + has_odd_freq

