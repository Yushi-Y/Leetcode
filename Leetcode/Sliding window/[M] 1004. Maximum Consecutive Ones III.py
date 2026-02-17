# This is sliding window again. Think of it as: find the longest window that contains at most k zeros. Expand right, and when you have more than k zeros in the window, shrink from left until you're back to ≤ k zeros. Track the max window length.

# For TC O(n): Just track zeros incrementally — when you expand right, check if nums[right] == 0 and increment a counter. When you shrink left, check if nums[left] == 0 and decrement it.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        count_k = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count_k += 1 # TC O(n)

            while count_k > k: # allow to have exactly k zeros
                if nums[left] == 0:  # check the current left before moving it
                    count_k -= 1
                left += 1
        
            max_len = max(max_len, right - left + 1)

        return max_len 



### My original code idea
# for right in range(len(nums)):
#     while nums[left:right+1].count(0) > k:
#         left += 1

#     max_len = max(max_len, right - left + 1)

# This works but count(0) scans the whole subarray every time, making it O(n²) instead of O(n). That's why tracking the count incrementally (add when expanding, subtract when shrinking) is better — interviewers will expect the O(n) version.
                


        
        