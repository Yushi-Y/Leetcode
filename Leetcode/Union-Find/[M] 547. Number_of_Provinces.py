# 牌子 = parent 数组
# pythonparent = [0, 1, 2]
# ```

# 就是：
# ```
# 城市0的牌子写着「0」 → 自己是老大
# 城市1的牌子写着「1」 → 自己是老大
# 城市2的牌子写着「2」 → 自己是老大
# Find = 顺着牌子一直看，直到找到写着自己名字的人
# def find(x):
#     while x != parent[x]:   # 牌子上写的不是自己？
#         x = parent[x]       # 去看牌子上那个人的牌子
#     return x                 # 找到老大了
# Union = 让一个老大把牌子擦掉，写上另一个老大的名字
# def union(x, y):
#     px, py = find(x), find(y)   # 找到两人的老大
#     if px != py:
#         parent[px] = py          # 一个老大的牌子改成另一个老大


# 目标
# 给你一堆城市和它们的连接关系，问你一共有几个省份（几个组）。
# 整体流程：三步
# 第一步：发牌子
# pythonparent = list(range(row))   # [0, 1, 2]
# 给每个城市发一个牌子，上面写自己的名字。意思是：一开始每个城市都是自己一组，自己是老大。
# 第二步：看连接，合并组
# pythonfor i in range(row):
#     for j in range(i + 1, col):
#         if isConnected[i][j] == 1:
#             union(i, j)
# 翻看连接表，每发现两个城市相连，就让它们成为一组。怎么合并？找到两边的老大，让一个老大把牌子改成另一个老大的名字。
# 第三步：数老大
# pythonfor i in range(row):
#     if find(i) == i:
#         count += 1
# ```

# 一个组只有一个老大（牌子上写着自己名字的人）。数有几个老大 = 有几个组 = 有几个省份。

# ## 就这样
# ```
# 发牌子 → 合并 → 数老大 → 得到答案
# 并查集所有题都是这个套路，只是"什么时候合并"的条件不同。这道题是 isConnected[i][j] == 1 时合并，换道题可能是别的条件，但 find、union、数老大的逻辑完全一样。


# Time Complexity: O(n²)

# 遍历上三角矩阵：O(n²)
# 每次 union/find 近似 O(1)（如果加路径压缩的话）
# 总共：O(n²)

# Space Complexity: O(n)

# parent 数组：O(n)
# 就这一个额外空间


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        row = len(isConnected)
        col = len(isConnected[0])

        parent = list(range(row))

        # 顺着上级一直往上找，直到找到老大（上级是它自己的人）
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
        # 看每两个城市之间有没有连接，有的话就分到一组
        for i in range(row):
            for j in range(i + 1, col):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        count = 0
        for i in range(row):
            if find(i) == i:
                count += 1 # 谁的老大是自己？就是 find(i) == i 的人
            
        return count 
        