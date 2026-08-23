# LeetCode 704. Binary Search（ACM 格式）
# 题目：
# 给定一个升序排列的整数数组 nums（元素互不相同）和一个目标值 target，如果 target 存在于数组中，返回其下标，否则返回 -1。
# 要求时间复杂度 O(log n)。
# 输入格式：

# 第一行：n 个空格分隔的整数，表示升序数组 nums
# 第二行：一个整数 target

# 输出格式：

# 一个整数，target 的下标（0-indexed），不存在则输出 -1

# 样例 1：
# 输入:
# -1 0 3 5 9 12
# 9

# 输出:
# 4
# 样例 2：
# 输入:
# -1 0 3 5 9 12
# 2

# 输出:
# -1

### Thoughts - 二分法查找
# mid = (left + right) // 2
# 如果nums[mid] == target, return True
# if nums[mid] < target, then target is in the right half - left = mid + 1
# else left half - right = mid - 1

import sys

def binary_search(nums, target):
    left, right = 0, len(nums)

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1



def main():
    inputs = sys.stdin.read().splitlines()
    nums = list(map(int, inputs[0].split()))
    target = int(inputs[1])

    print(binary_search(nums, target))



