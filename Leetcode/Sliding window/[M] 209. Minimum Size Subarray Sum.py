# Use a sliding window because all numbers are positive — expanding always increases the sum, shrinking always decreases it. Expand right until the sum ≥ target, then keep shrinking from left as long as the window is still valid, updating the minimum length each time. 

# By trying every right (for loop), you guarantee you've considered all possible ending positions. For each ending position, the while loop finds the tightest (leftmost) starting point. So together, you've checked every possible shortest window.

# TC O(n), SC O(1)
# Total work: right visits each element once (n) + left visits each element at most once (n) = O(2n) = O(n).

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        value = 0
        min_len = float('inf')

        for right in range(len(nums)):
            value += nums[right]

            while value >= target:
                min_len = right - left + 1
                value -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
    
        
        