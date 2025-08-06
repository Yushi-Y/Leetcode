# (Easy) Running Sum of 1d Array
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

