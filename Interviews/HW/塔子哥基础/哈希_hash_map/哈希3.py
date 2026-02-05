import sys
from collections import defaultdict

# count how many a_1, ..., a_n = n

def count_prefix(n, arr):
    counts = []
    H = defaultdict(int)

    # for x in arr:
    #     H[x] += 1
    
    for j in range(1, n + 1):
        H[arr[j - 1]] += 1
        counts.append(H.get(j - 1, 0))

    return counts


def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    counts = count_prefix(n, arr)

    print(' '.join(map(str, count)))

if __name__ == "__main__":
    main()
