# LeetCode 240. Search a 2D Matrix II（ACM 格式）——华为矩阵题出场率之王
# 题目：
# 给定一个 m × n 整数矩阵 matrix，具有以下性质：

# 每行元素从左到右升序排列
# 每列元素从上到下升序排列

# 给定目标值 target，判断它是否在矩阵中。
# 输入格式：

# 第一行：两个整数 m 和 n
# 接下来 m 行：每行 n 个空格分隔的整数
# 最后一行：一个整数 target

# 输出格式：

# true 或 false

# 样例 1：
# 输入:
# 5 5
# 1 4 7 11 15
# 2 5 8 12 19
# 3 6 9 16 22
# 10 13 14 17 24
# 18 21 23 26 30
# 5

# 输出:
# true


### Thoughts
# 关键区别提醒： 这题和 74 不同——74 是"上一行末尾 < 下一行开头"，整个矩阵摊平就是有序一维数组，能直接二分。240 只保证行有序、列有序，比如样例里 15（第一行末）> 2（第二行头），摊平不了。
# 所以经典解法不是二分，是 staircase search：从某个角落出发，每次比较能排除一整行或一整列，O(m + n)。
# 思考题：四个角，从哪个角出发才行？提示——想想在那个位置上，matrix[i][j] > target 和 < target 分别告诉你什么。左上角为什么不行？
# right bottom is largest, 往上、往左都只会变小。也就是说当 matrix[row][col] < target 时，你两个方向都没救——这个角上"太小"和"太大"两种情况只有一个方向可走，排除不了另一半
# left top is smallest and must < target, so no
# 左下角，从行来说（往上）会变小，从列来说（往右）会变大
# 右上角也可以，移动方向反一反就行

import sys

def search(matrix, target):
    m, n = len(matrix), len(matrix[0])
    row, col = m - 1, 0

    while 0 <= row < m and 0 <= col < n:
         if matrix[row][col] == target:
             return True
         elif matrix[row][col] < target:
             col += 1 # 往右
         else:
             row -= 1 # 往上
             
    return False
             

def main():
    inputs = sys.stdin.read().splitlines()
    m, n = map(int, inputs[0].split())
    target = int(inputs[-1])
    matrix = [list(map(int, row.split())) for row in inputs[1:m+1]]
    print("true" if search(matrix, target) else "false")

main()