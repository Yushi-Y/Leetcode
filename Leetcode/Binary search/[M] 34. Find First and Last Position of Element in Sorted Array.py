class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search, need to do twice
        # TC(logn)
        n = len(nums)

        # edge case - empty list
        if not nums:
            return [-1, -1]
        
        start_index = self.find_start(nums, target)
        end_index = self.find_end(nums, target)

        if start_index > end_index: # target does not exist
            return [-1, -1]
        else:
            return [start_index, end_index]

# find_start: Find the LEFTMOST target
# When you see the target, don't stop — there might be more copies to the LEFT
# So you move right to keep searching left

# find_end: Find the RIGHTMOST target
# When you see the target, don't stop — there might be more copies to the RIGHT
# So you move left to keep searching right

# find_start: nums[mid] < target — when nums[mid] == target, it falls into the else, so right = mid - 1. This pushes the search leftward, squeezing past equal elements to find the first one. Returns left.
# find_end: nums[mid] <= target — when nums[mid] == target, it stays in the if, so left = mid + 1. This pushes the search rightward, squeezing past equal elements to find the last one. Returns right.
# So the = decides which direction you keep searching when you're sitting on a match.

    def find_start(self, nums, target):
        left, right = 0, len(nums) - 1 # index

        # find starting index of target
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else: 
                right = mid - 1

        return left

    def find_end(self, nums, target):
        left, right = 0, len(nums) - 1 # index

        # find ending index of target
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
            else: 
                right = mid - 1

        return right



        