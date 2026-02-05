### Hashmap solution
# TC: O(n)
# SC: O(n)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = {} # a hashmap, or a dict

#         for num in nums:
#             count[num] = count.get(num, 0) + 1
#             if count[num] > len(nums) / 2:
#                 return num


### Sorting solution
# TC: O(nlogn) - dominated by sort
# SC: O(1) - nothing to store
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() # O(nlogn) # ascending
        return nums[len(nums) // 2] # def cover the middle element
