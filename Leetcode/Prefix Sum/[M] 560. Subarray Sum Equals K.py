# If two prefix sums differ by k, the subarray between them sums to k. So for each prefix sum, we check how many times prefix_sum - k has appeared before.

# Given an array nums = [1, 3, 5, 2, 4], the prefix sum array would be [1, 4, 9, 11, 15].

# Time: O(n) — single pass through the array, with O(1) hashmap lookups.
# Space: O(n) — the seen hashmap can store up to n + 1 distinct prefix sums.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        # Maps prefix_sum -> how many times we've seen it
        seen = {0: 1}  # base case: empty prefix (1 example) has sum 0

        for num in nums:
            prefix_sum += num
            # If (prefix_sum - k) was seen before, those are valid subarrays
            count += seen.get(prefix_sum - k, 0) 
            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        return count


        