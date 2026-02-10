class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        row = len(isConnected)
        col = len(isConnected[0])

        parent = list(range(row))

        # 顺着上级一直往上找，直到找到老大（上级是自己的人）
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        # 找到两个人的老大，让一个老大认另一个当老大
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        # 只需要遍历矩阵的上三角（即 j > i 的部分），因为矩阵是对称的
        for i in range(row):
            for j in range(i + 1, col):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        count = 0
        for i in range(row):
            if find(i) == i:
                count += 1 # 谁的老大是自己？就是 find(i) == i 的人
            

        return count 
        