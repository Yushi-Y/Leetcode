mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

# dfs[i] -> dfs[i + 1], i is the i-th digits (index of digits)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        ans = []
        path = [''] * n # path in one output string

        def dfs(i):
            if i == n:
                ans.append(''.join(path))
                return

            # list what i is
            for c in mapping[int(digits[i])]:
                path[i] = c
                dfs(i + 1)

        dfs(0)
        return ans
                



        