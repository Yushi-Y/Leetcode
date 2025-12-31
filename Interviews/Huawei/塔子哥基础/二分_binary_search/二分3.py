import sys


def find_pre(arr, target):
    n = len(arr)

    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else: 
            right = mid - 1
    if right < 0:
        return -1
    else:
        return arr[right]


def find_after(arr, target):
    n = len(arr)

    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        else: 
            left = mid + 1
    if left >= n: # index valid from 0 to n - 1
        return -1
    else:
        return arr[left]


def main():
    lines = sys.stdin.read().strip().splitlines()
    n, Q = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    for i in range(Q):
        target = int(lines[2 + i])
        pre_value = find_pre(arr, target)
        after_value = find_after(arr, target)
        print(f'{pref_value} {after_value}')
    

if __name__ == "__main__":
    main()