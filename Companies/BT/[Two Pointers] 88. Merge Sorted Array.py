# Problem 1 — LC 88: Merge Sorted Array
# You are given two sorted integer arrays nums1 and nums2, 
# and integers m and n representing the number of valid elements in each. 
# nums1 has length m + n, with the last n slots filled with zeros as placeholders. 
# Merge nums2 into nums1 so that nums1 is sorted in non-decreasing order, in place (O(1) extra space).

# Input format:
# Line 1: m n
# Line 2: m + n integers (nums1, trailing zeros included; empty line if m + n = 0)
# Line 3: n integers (nums2; empty line if n = 0)

# Output format:
# The merged array, space-separated, on one line
# Example:
# Input:
# 3 3
# 1 2 3 0 0 0
# 2 5 6

# Output:
# 1 2 2 3 5 6
# Constraints: 0 ≤ m, n ≤ 200; −10⁹ ≤ values ≤ 10⁹.

### ACM
# 输入:
# Line 1: 两个整数 m n (空格分隔)
# Line 2: m+n 个整数 — nums1, 末尾 n 个为占位 0; 若 m+n=0 则为空行
# Line 3: n 个整数 — nums2; 若 n=0 则为空行

# 输出:
# 一行, 合并后的数组, 空格分隔

### Thoughts
# 为什么不能从前往后合并
# nums1 = [1, 2, 3, 0, 0, 0]   m = 3
# nums2 = [2, 5, 6]            n = 3
# 假设从前面开始:比较 nums1[0]=1 和 nums2[0]=2,1 更小,没问题。
# 下一步比较 nums1[1]=2 和 nums2[0]=2,假设我们想把 nums2 的 2 放进 nums1[1]——但 nums1[1] 现在存着有效数据 2,一旦写入就把原来的数覆盖丢失了。
# 要不丢数据就得先把后面的元素全部右移,那就变成 O(m·n) 了。
# 所以反过来想:从后往前填。整个合并后的数组,最后一个位置(index 5)应该放什么?应该放所有数里最大的那个。最大的数只可能是两个数组各自的最后一个有效元素之一:
# nums1 有效末尾: nums1[2] = 3
# nums2 末尾:     nums2[2] = 6
# 比较 → 6 更大 → 把 6 写到 nums1[5]

# [1, 2, 3, 0, 0, 6]
# 写完之后,6 已经"用掉了",nums2 的指针左移一格。继续问:index 4 应该放什么?剩下的数里最大的:
# 比较 nums1[2]=3 和 nums2[1]=5 → 5 更大 → 写到 nums1[4]
# [1, 2, 3, 0, 5, 6]
# 再来:
# 比较 nums1[2]=3 和 nums2[0]=2 → 3 更大 → 写到 nums1[3]
# [1, 2, 3, 3, 5, 6]
#       ↑     ↑
#       注意 nums1[2] 的 3 被复制到了 nums1[3],原位置的 3 现在是垃圾——没关系,它已经被安全搬走了

# 为什么从后往前永远不会覆盖?
# 写入位置 k 从末尾往左走,读取位置 i 也在往左走,而且 k 永远在 i 的右边(k 每次消耗一个元素,i 最多左移一格),所以写入的地方要么是占位 0,要么是已经搬走的旧数据。

# 三个指针总结
# i = m - 1        # nums1 有效部分的最后一个
# j = n - 1        # nums2 最后一个
# k = m + n - 1    # 当前要填的位置
# 每一轮: 比较 nums1[i] 和 nums2[j],大的写进 nums1[k],对应指针和 k 都左移

# 用一个具体例子走一遍:
# nums1 = [4, 5, 6, 0, 0, 0]   m = 3
# nums2 = [1, 2, 3]            n = 3
# 从后往前合并:
# 比较 6 和 3 → 6 大 → nums1[5] = 6, i 左移
# 比较 5 和 3 → 5 大 → nums1[4] = 5, i 左移
# 比较 4 和 3 → 4 大 → nums1[3] = 4, i 左移 → i = -1,循环退出

# 此时 nums1 = [4, 5, 6, 4, 5, 6]
#               ↑  ↑  ↑
#               这三个位置还没被填过!
# 循环退出了,因为 nums1 的有效元素用完了(i < 0)。但 nums2 的 [1, 2, 3] 一个都还没搬过去——j 还停在 2。它们应该去哪?去 nums1[0..2]。可现在那里放的是旧的垃圾数据 4, 5, 6。
# 所以循环后需要补一段:把 nums2 剩下的 nums2[0..j] 逐个复制到 nums1 对应位置。
# 那为什么 nums1 先剩下就不用管? 反过来的例子:
# nums1 = [1, 2, 3, 0, 0, 0]   m = 3
# nums2 = [4, 5, 6]            n = 3

# 比较 3 和 6 → nums1[5] = 6
# 比较 3 和 5 → nums1[4] = 5
# 比较 3 和 4 → nums1[3] = 4 → j = -1,退出

# 此时 nums1 = [1, 2, 3, 4, 5, 6]
#               ↑  ↑  ↑
#               没被循环碰过,但它们本来就在正确的位置上
# nums1 剩余的元素已经住在自己家里,不需要搬;nums2 剩余的元素还在别的数组里,必须搬过来。这就是不对称的原因。


import sys

def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0: # and k > 0

        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i] 
            i -= 1
        else:
            nums1[k] = nums2[j] 
            j -= 1

        k -= 1

    # 如果nums2部分还有剩余，要直接填入nums1里面
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1

    

def main():
    data = sys.stdin.read().splitlines()
    m, n = map(int, data[0].split())
    nums1 = list(map(int, data[1].split()))
    nums2 = list(map(int, data[2].split()))
    
    output_nums1 = merge(nums1, m, nums2, n)
    print(' '.join(map(str, output_nums1)))


main()
