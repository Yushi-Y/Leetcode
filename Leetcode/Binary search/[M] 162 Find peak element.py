class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        while left < right: 
            mid = left + (right - left) // 2 # need to update mid in loop!

            if nums[mid] > nums[mid + 1]: # peak is from left to mid
                right = mid
            else: # peak at right side (exclude mid)
                left = mid + 1

        return left # or right, same thing as they converge


        