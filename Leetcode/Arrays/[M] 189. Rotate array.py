# (Easy) Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums) # replace k with the remainer, so k is not out-of-bounds
        nums[:] = nums[-k:] + nums[:-k] # last k elements + first (n-k) elements
        return nums

