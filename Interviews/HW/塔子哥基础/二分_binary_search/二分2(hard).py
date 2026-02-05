import sys

# use L pointer to find the smallest index T, R stops at T - 1 (before T)
def find_smallest_index(arr, q):
    n = len(arr)

    left, right = 0, n - 1 
    while left <= right: 
        mid = (left + right) // 2 # middle index
        if arr[mid] >= q:
            right = mid - 1
        else: # arr[mid] < q:
            left = mid + 1
    if left > n - 1 or arr[left] != q: # q not in array
        return -1
    else:
        return left

# use R pointer to find the largest index T, L stops at T + 1 (after T)
def find_largest_index(arr, q):
    n = len(arr)

    left, right = 0, n - 1 
    while left <= right: 
        mid = (left + right) // 2 # middle index
        if arr[mid] <= q:
            left = mid + 1
        else: # arr[mid] > q:
            right = mid - 1
    if right < 0 or arr[right] != q:
        return -1
    else:
        return right


def main():
    lines = sys.stdin.read().strip().splitlines()

    n, Q = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))

    queries = []
    for i in range(Q):
        query = int(lines[2 + i])
        left_index = find_smallest_index(arr, query)
        right_index = find_largest_index(arr, query)
        print(f'{left_index + 1} {right_index + 1}') # convert to 1-based indexes


if __name__ == "__main__":
    main()