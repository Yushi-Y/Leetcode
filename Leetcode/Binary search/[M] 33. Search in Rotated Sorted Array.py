# binary search TC O(logn), SC O(1)
# two halves in the array

# at least one half of the array is sorted 
# decide which half (left or right), then check if the target is in that half using binary search
# move the left and right pointers accordingly

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


        # basic template of binary search
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target: # then target in the right half
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        
        # return -1
        


        