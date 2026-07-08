# 70. Climbing Stairs
# 你正在爬楼梯。需要 n 阶才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶？
# 示例 1:
# 输入: n = 2
# 输出: 2
# 解释: 1+1 或 2
# 示例 2:
# 输入: n = 3
# 输出: 3
# 解释: 1+1+1, 1+2, 2+1
# 约束: 1 <= n <= 45

### Thoughts
# recusion: f(n) = f(n - 1) + f(n - 2) - fibonacci
# base case: f(1) = 1, f(2) = 2

### TC: O(n)
### SC: O(n)

import sys


# 滚动变量提示:

# 你只需要记住"前两阶"的答案。设两个变量:

# prev2 = 爬 i-2 阶的方法数
# prev1 = 爬 i-1 阶的方法数


# 每轮循环:

# 当前答案 cur = prev1 + prev2
# 然后滚动:旧的 prev1 变成新的 prev2,cur 变成新的 prev1

def solve(n):
    if n <= 2:
        return n
    
    prev2, prev1 = 1, 2

    for i in range(3, n + 1):
        cur = prev1 + prev2
        prev2 = prev1
        prev1 = cur

    return cur

# def solve(n):
#     if n == 1:
#         return 1
    
#     ways = [0] * n # 0 to n-1
#     ways[0] = 1
#     ways[1] = 2
#     for i in range(2, n):
#         ways[i] = ways[i - 1] + ways[i - 2]

#     return ways[n - 1]

### ACM
n = int(sys.stdin.readline())   # 或 int(sys.stdin.readline())
print(solve(n))

