class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)

# f[j] = edit distance between word1[:i] → word2[:j]
# i = how many characters of word1 we’ve processed (outer loop)
# j = how many characters of word2 we’ve processed (inner loop)
# So f represents one DP row.

        # O(nm), O(m) - 1d array
        f = list(range(m + 1)) # it takes j steps to convert to word2[:j] from an EMPTY string
        for i, x in enumerate(word1):
            prev = f[0]
            f[0] = i + 1

            for j, y in enumerate(word2):
                tmp = f[j + 1]
                f[j + 1] = prev if x == y else min(f[j], f[j+1], prev) + 1
                prev = tmp
        return f[m]



        # O(nm), O(nm)
        # DFS + memoization = Top-down DP
        # f = [[0] * (m + 1) for _ in range(n + 1)]
        # # specify 0-condition to ensure correct transition
        # for j in range(m):
        #     f[0][j] = j
        # for i in range(n):
        #     f[i][0] = i
        # for i, x in enumerate(word1):
        #     for j, y in enumerate(word2):
        #         if x == y:
        #             f[i+1][j+1] = f[i][j] 
        #         else: 
        #             f[i+1][j+1] = min(f[i+1][j], f[i][j+1], f[i][j]) + 1

        # return f[n][m]


        # O(3^n) without memorisation (array)
        # @cache
        # def dfs(i, j):
        #     if i < 0:
        #         return j + 1 (+1 as zero indexed)
        #     if j < 0:
        #         return i + 1
        #     if word1[i] == word2[j]:
        #         return dfs(i-1, j-1) 
        #     return min(dfs(i, j-1), dfs(i-1, j), dfs(i-1, j-1)) + 1

        # return dfs(n-1, m-1) (zero-indexed, so last index is n - 1)
        