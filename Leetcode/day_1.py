# Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Returns the running sum of an array nums.
        """
        running_sum = []
        sum_so_far = 0
        for num in nums:
            sum_so_far += num
            running_sum.append(sum_so_far)
        return running_sum



# Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Returns the pivot index of an array nums. If no such index exists, return -1.
        """
        left_sum = 0
        right_sum = sum(nums)
        for i, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return i
            left_sum += num
        return -1


