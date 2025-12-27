import sys
from collections import defaultdict

# a[i] + a[j] = i + j, i < j
# j - a[j] = a[i] - i, loop throug j
# For each j, create a hash map of counts for a[i] - i for i < j

def count_equal_sum(arr):
    count = 0
    H = defaultdict(int)
    n = len(arr)

    for j in range(1, n + 1):
        a_j = arr[j - 1]
        look_up = a_j - j
        count += H.get(look_up, 0)
        H[look_up] += 1

    return count

def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    count = count_equal_sum(arr)
    print(count)

if __name__ == "__main__":
    main()