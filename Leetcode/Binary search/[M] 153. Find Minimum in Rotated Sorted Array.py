# A rotated sorted array has two sorted halves. The minimum element is the "pivot point" where the rotation happened — it's the only element smaller than its predecessor.

# You need O(log n), so binary search. The key question at each step: how do you decide whether to go left or right? Think about what you can compare nums[mid] against to determine [which half the minimum lives in].

# Compare nums[mid] with nums[right]:
# If nums[mid] > nums[right] → what does that tell you about which side the pivot/minimum is on?
# If nums[mid] <= nums[right] → what does that tell you?

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None

        n = len(nums)
        left, right = 0, n - 1

        while left < right: # use <, otherwise infinite loop when left == right and right = mid never moves
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid # not mid - 1 for the [3,1,2] case, not miss the mid = 1

        return nums[left]



        