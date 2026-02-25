# Key insight: Replace every odd number with 1 and every even with 0. Now it's exactly problem 560 — subarray sum equals k.
# TC O(n), SC O(n)

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        seen = {0: 1}
        prefix_sum = 0

        for num in nums:
            # if num % 2 == 1:
            #     num = 1
            # else:
            #     num = 0
            prefix_sum += num % 2 # easier way to add 0 or 1
            count += seen.get(prefix_sum - k, 0)
            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        return count

            
        