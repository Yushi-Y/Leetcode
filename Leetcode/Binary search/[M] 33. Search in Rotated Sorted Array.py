# binary search TC O(logn), SC O(1)
# two halves in the array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right: 
            mid = (left + right) // 2 # update in while loop!

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:  # if target in left range
                    right = mid - 1
                else: 
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:  # if target in left range
                    left = mid + 1
                else: 
                    right = mid - 1

        return -1

        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target: # then target in the right half
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        
        # return -1
        


        