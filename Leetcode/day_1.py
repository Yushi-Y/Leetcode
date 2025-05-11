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
        
# Time complexity: O(n) - for loop
# Space complexity: O(n) - store the running_sum list


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

# Time complexity: O(n) (computing the sum) + O(n) (for loop) = O(n)
# Space complexity: O(1) - only left_sum and right_sum are stored, both O(1)


