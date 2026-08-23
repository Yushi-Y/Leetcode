# 题目：
# 给定一个按非递减顺序排列的整数数组 nums（可能有重复元素）和一个目标值 target，找出 target 在数组中的开始位置和结束位置。
# 如果 target 不存在，返回 -1 -1。
# 要求时间复杂度 O(log n)。
# 输入格式：

# 第一行：n 个空格分隔的整数，表示非递减数组 nums
# 第二行：一个整数 target

# 输出格式：

# 两个空格分隔的整数：开始下标和结束下标

# 样例 1：
# 输入:
# 5 7 7 8 8 10
# 8

# 输出:
# 3 4
# 样例 2：
# 输入:
# 5 7 7 8 8 10
# 6

# 输出:
# -1 -1


### Thoughts - 二分法查找 - Very similar to 704
# mid = (left + right) // 2
# 如果nums[mid] == target, return True
# if nums[mid] < target, then target is in the right half - left = mid + 1
# else left half - right = mid - 1

import sys

def search_bound(nums, target, find_first):
    left, right = 0, len(nums) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            ans = mid
            if find_first:
                right = mid - 1  # 命中最左的，要往左边继续收缩
            else:
                left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ans



def main():
    inputs = sys.stdin.read().splitlines()
    nums = list(map(int, inputs[0].split()))
    target = int(inputs[1])

    first = search_bound(nums, target, True)
    last = search_bound(nums, target, False)
    print(first, last)

main()