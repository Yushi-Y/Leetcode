# Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
   # Returns the index of the target value in an array of integers in ascending order, or -1 if the target is not found.
   # O(log n) implies that need to use binary search, not linear search O(n)
   # Binary Search: Maintaining two pointers: left and right (initially pointing to the first and last index). Repeatedly narrowing the search space by comparing the middle element to the target. Halving the search space each time.
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
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


