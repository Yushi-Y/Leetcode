# (Easy) Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums) # ensure k is within bounds of the array
        nums[:] = nums[-k:] + nums[:-k]

