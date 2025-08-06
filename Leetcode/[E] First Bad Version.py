# (Easy) First Bad Version
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        ### Binary search - O(log2(n)) - The number of iterations is proportional to how many times you can divide n by 2 until you narrow it to a single point.
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


### Linear search O(n)
# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         for i in range(1, n + 1):
#             if isBadVersion(i):
#                 return i
#         return -1