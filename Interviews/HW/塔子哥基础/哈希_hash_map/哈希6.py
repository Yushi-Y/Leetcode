import sys
from collections import defaultdict


# find numbers of (i, j, k) pairs 
# such that a[i] = a[j] + 1 = a[k] and 1 <= i < j < k <= n
# want to list j such as two maps
# map 1: a[i] = a[j] + 1 for i < j
# map 2: a[k] = a[j] + 1 for j < k

def count_three_sum(arr):
    n = len(arr)
    if n <= 2:
        return 0

    H_prev = defaultdict(int) # keep empty
    H_after = defaultdict(int)
    for num in arr:
        H_after[num] += 1  # full list

    total = 0
    for j in range(1, n + 1):
        value = arr[j - 1]
        target = value + 1

        # remove current from after so it counts only elements after j
        H_after[value] -= 1

        count_prev = H_prev.get(target, 0)
        count_after = H_after.get(target, 0)

        # add current element to previous for future j
        H_prev[value] += 1

        total += count_prev * count_after

    return count


def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    count = count_three_sum(arr)
    print(count)


if __name__ == "__main__":
    main()