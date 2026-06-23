import sys
from collections import defaultdict

# implicit left in two-pointer
def count_len(red_nums, blue_nums):
    n = len(red_nums)
    max_len = 0 
    current = 0

    for i in range(1, n):
        diff_r = red_nums[i] - red_nums[i - 1]
        diff_b = blue_nums[i] - blue_nums[i - 1]
        if diff_r == diff_b: 
            current += 1 
            max_len = max(max_len, current)
        else:
            current = 0

    return max_len if max_len <= n else -1


def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    print(count_len(nums))


if __name__ == "__main__":
    main()