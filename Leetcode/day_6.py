# Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Returns the index of the target value in an array of integers in ascending order,
        or -1 if the target is not found.
        """
        # Initialise two pointers
        left, right = 0, len(nums) - 1

        # Binary search - reduce the search space by half in each iteration
        # Time complexity is O(log(n)), as maximum iterations are log2n times
        while left <= right:
            # Compare the target with the middle element
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # The while loop ends when left > right        
        return -1



# First Bad Version
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        """
        Returns the index of the first bad version of a product from a list of n versions.
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left



# Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


