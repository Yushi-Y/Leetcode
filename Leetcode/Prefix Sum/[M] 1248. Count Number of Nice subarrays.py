# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.


# Prefix sum: If prefix[j] - prefix[i] == k, then the subarray (i, j] is nice. So for each j, you want to count how many previous prefix sums equal prefix[j] - k.
# look up the frequency in a hashmap, so O(n)
# TC: O(n) - — single pass through the array in for loop, hashmap look up is O(1).
# SC: O(n) — the hashmap stores at most n+1 distinct prefix sums.
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0

        hashmap = {0: 1}
        running_sum = 0

        for num in nums:
            running_sum += 1 if num % 2 == 1 else 0
            count += hashmap.get(running_sum - k, 0) # use .get to give default 0 for no such key
            hashmap[running_sum] = hashmap.get(running_sum, 0)

        return count



# Sliding window: exactly(k) = atMost(k) - atMost(k-1), where atMost(k) counts subarrays with at most k odd numbers.
# atMost(k) counts subarrays with at most k odd numbers
# atMost(k): expand right, shrink left when odd count exceeds k
# O(n) time, O(1) space

# Expand right, increment odd count if nums[right] is odd
# While odd count > k, shrink left
# At each right, add right - left + 1 (all subarrays ending at right)


class Solution:
    def atMost(self, k, nums):
        left = 0
        odds = 0
        count = 0

        for right in range(len(nums)):
            odds += nums[right] % 2 
            while odds > k:
                odds -= nums[left] % 2
                left += 1
            count += right - left + 1

        return count

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(k, nums) - self.atMost(k - 1, nums)
