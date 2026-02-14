# 树 = 没有环（cycle）的连通图。 多了一条边 = 某条边让图产生了环。
# 用并查集的思路想：遍历每条边，做 union 之前先 find 一下——如果两个节点的老大已经相同，说明什么？
# 说明它们已经在同一组了，再加这条边就会形成环 → 这条边就是多余的。

# 遍历每条边 [x, y]：
#   1. 先看 x 和 y 的老大是不是同一个
#   2. 如果是 → 已经在同一组了，再加这条边就成环 → 返回这条边
#   3. 如果不是 → 合并它们

# TC: O(n)，遍历 n 条边，每次 find 近似 O(1)
# SC: O(n)，parent 数组

# edges = [[1,2],[1,3],[2,3]]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # col = len(edges[0])

        parent = list(range(n + 1)) # 节点是1到n+1

        def find(x): # 找到node x 的老大
            while x != parent[x]:
                x = parent[x]
                
            return x

        def union(x, y): # 把联通的两个node的老大换成一个
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        for x, y in edges:
                if find(x) == find(y):
                    return [x, y]
                union(x, y)

            

    
        