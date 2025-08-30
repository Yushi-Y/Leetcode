# Binary Search
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Two-pointer sorting: O(n) - more efficient
        n = len(nums)
        squared_list = [0] * n
        left, right = 0, n - 1,
        for i in range(n - 1, -1, -1): # start, stop, step
            if abs(nums[right]) < abs(nums[left]): 
                squared_list[i] = nums[left] ** 2
                left += 1
            else:
                squared_list[i] = nums[right] ** 2      
                right -= 1 
        return squared_list  
    

# Normal sorting: O(nlogn)
# def sortedSquares(self, nums: List[int]) -> List[int]:
#     n = len(nums)
#     squared_list = [0] * n                  # O(n) to allocate
#     for i in range(n):                      # O(n) to fill with squares
#         squared_list[i] = nums[i] ** 2
    
#     squared_list = sorted(squared_list)     # O(n log n) sorting - dominant term
#     return squared_list