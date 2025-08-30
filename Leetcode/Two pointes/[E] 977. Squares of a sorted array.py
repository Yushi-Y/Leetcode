# (Easy)Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Returns an array of the squares of each number in nums, sorted in non-decreasing order.
        """
        n = len(nums)
        squares = [0] * n
        # Initialize two pointers
        left, right = 0, n - 1

        # Iterate from n-1 down to 0
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                # Appends the square of the element at left to the squares array 
                squares[i] = nums[left] ** 2
                # Increment the left
                left += 1
                
            else:
                squares[i] = nums[right] ** 2
                right -= 1
                
        return squares
        

