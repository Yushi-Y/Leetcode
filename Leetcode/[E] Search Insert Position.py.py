# (Easy) Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # index = nums.index(target) if target in nums else -1 
        # index = [i for i, x in emnumerate(nums) if x == target]
        # Binary search
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 # midpoint
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return left

