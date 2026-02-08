
# Lingshen solution 1
# dfs(i, c) - number of ways to make amount c using first i numbers
# Time complexity: O(n*target) - n is the number of elements in nums
# Space complexity: O(n*target) - recursion stack and cache
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # p - all positive numbers sum, i.e. coins we added (+)
        # s - p
        # p - (s - p) = 2p - s = target
        # p = (target + s) / 2

        n = len(nums)
        target += sum(nums)
        target //= 2


        # @cache
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            if c < nums[i]:
                return dfs(i - 1, c)
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])
        
        return dfs(n - 1, target)
    




# Lingshen solution 2
# dfs(i, c) - number of ways to make amount c using first i numbers
# Time complexity: O(n*target) - n is the number of elements in nums
# Space complexity: O(n * target) 
# f[i + 1][c] = f[i][c] + f[i][c - nums[i]]

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # p - all positive numbers sum, i.e. coins we added (+)
        # s - p
        # p - (s - p) = 2p - s = target
        # p = (target + s) / 2

        n = len(nums)
        target += sum(nums)
        target //= 2


        f = [[0] * (target + 1) for _ in range(n + 1)] 
        f[0][0] = 1

        for i, x in enumerate(nums):
            for c in range(target + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = f[i][c] + f[i][c - nums[i]]

        return f[n][target]

        # # @cache
        # def dfs(i, c):
        #     if i < 0:
        #         return 1 if c == 0 else 0
        #     if c < nums[i]:
        #         return dfs(i - 1, c)
        #     return dfs(i - 1, c) + dfs(i - 1, c - nums[i])
        
        # return dfs(n - 1, target)
    




        

# Lingshen solution 3
# dfs(i, c) - number of ways to make amount c using first i numbers
# Time complexity: O(n) - n is the number of elements in nums
# Space complexity: O(n) 
# f[c] = f[c] + f[c - nums[i]]

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # p - all positive numbers sum, i.e. coins we added (+)
        # s - p
        # p - (s - p) = 2p - s = target
        # p = (target + s) / 2

        n = len(nums)
        target += sum(nums)
        target //= 2


        f = [0] * (target + 1)
        f[0] = 1

        for num in nums:
            for c in range(target, num - 1, -1):
                f[c] = f[c] + f[c - num]

        return f[target]

        # # @cache
        # def dfs(i, c):
        #     if i < 0:
        #         return 1 if c == 0 else 0
        #     if c < nums[i]:
        #         return dfs(i - 1, c)
        #     return dfs(i - 1, c) + dfs(i - 1, c - nums[i])
        
        # return dfs(n - 1, target)
        