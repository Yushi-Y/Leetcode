# dfs(i) is the LIS for the seq ending with index i (does not have to start at index 0)
# dfs(i) = dfs(j) + 1 if j < i and nums[j] < nums[i]
# for arrays, f[i] = f[j] + 1 if j < i and nums[j] < nums[i]

# TC: O(n^2), SC: O(n)

### First solution: DP (DFS (recursion) with cache)
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         n = len(nums)

#         @cache # stores results in memory so each dfs(i) is only computed once
#         def dfs(i):
#             res = 0 # hold the best option at index i - 1, assume starting at 0
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     res = max(res, dfs(j)) # keep the best option at index i - 1
#             return res + 1 # then add the current positon

#         return max(dfs(i) for i in range(n))



### Second solution: array with for loop
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        f = [0] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[j], f[i])
            f[i] += 1

        return max(f)

       

        