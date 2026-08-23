# Given an array heights of n non-negative integers, where each value is the height of a bar in a histogram and every bar has width 1, return the area of the largest rectangle that fits entirely inside the histogram.

# Input:  heights = [2,1,5,6,2,3]
# Output: 10

# The 10 comes from the bars of height 5 and 6: take height 5 across both, width 2 → area 10.

# Input:  heights = [2,4]
# Output: 4

### Thoughts
# monotonic stack
# 用stack存逐渐递增的柱子的下标，也就是heights的index，不是实际高度
# 为什么必须存下标而不是高度?
# 因为你要算宽度。宽度 = 右边界位置 − 左边界位置 − 1。如果栈里只有高度,你根本不知道这根柱子在哪儿,减不出来。而反过来,有了下标随时能用 heights[j] 查到高度 —— 下标信息量更大,所以存下标。

# 栈里的每个下标 j,都是一根**"矩形还没结算完"的柱子**:它右边到目前为止还没出现比它更矮的东西,所以以 h[j] 为高的矩形还能继续往右长,面积未定,先押在栈里等着。
# 一旦某个 i 让 heights[i] < heights[j],j 的路走到头了,弹出来结算。


def largestrec(heights):
    max_area = 0
    stack = [-1]

    for i in range(len(heights)):
        while len(stack) > 1 and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    return max_area

