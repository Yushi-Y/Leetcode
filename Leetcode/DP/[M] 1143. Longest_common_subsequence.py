class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        # 1d array: TC O(nm), SC O(m)
        f = [0] * (m + 1)
        for x in text1:
            prev = 0 # f[0]
            for j, y in enumerate(text2):
                tmp = f[j + 1]
                f[j + 1] = prev + 1 if x == y else max(f[j], f[j+1])
                prev = tmp
        return f[m]

        # recursion: TC O(nm), SC O(nm)
        # f = [[0] * (m + 1) for _ in range(n + 1)]
        # for i, x in enumerate(text1):
        #     for j, y in enumerate(text2):
        #         f[i+1][j+1] = f[i][j] + 1 if x == y else max(f[i][j+1], f[i+1][j])
        # return f[n][m]


        # classic dfs: TC O(nm), SC O(nm)
        # @cache
        # def dfs(i, j):
        #     if i < 0 or j < 0:
        #         return 0

        #     if text1[i] == text2[j]:
        #         return dfs(i - 1, j - 1) + 1
        #     return max(dfs(i - 1, j), dfs(i, j - 1))

        # return dfs(n - 1, m - 1)
        