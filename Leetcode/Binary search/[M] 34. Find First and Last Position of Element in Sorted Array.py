class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search, need to do twice
        # TC(logn)
        n = len(nums)

        # edge cases
        if not nums:
            return [-1, -1]
        
        start_index = self.find_start(nums, target)
        end_index = self.find_end(nums, target)

        if start_index > end_index: # target does not exist
            return [-1, -1]
        else:
            return [start_index, end_index]

# find_start: Find the LEFTMOST target
# When you see the target, don't stop—there might be more copies to the LEFT
# So you move right to keep searching left

# find_end: Find the RIGHTMOST target
# When you see the target, don't stop—there might be more copies to the RIGHT
# So you move left to keep searching right

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






        # Two pointers, O(n)
        # if not nums:
        #     return [-1, -1]

        # left, right = 0, len(nums) - 1

        # while left <= right and nums[left] != target:
        #     left += 1

        # while left <= right and nums[right] != target:
        #     right -= 1 

        # if left > right: # so no target exists
        #     return [-1, -1]

        # return [left, right]


        