import sys

# For a given i, count the smallest and largest index of j such that a[j] = a[i] - target 
def count_pairs(arr, target):
    n = len(arr)
    count = 0

    for i in range(n):
        value = arr[i] - target
        small_index = find_smallest_index(arr, value)
        large_index = find_largest_index(arr, value)
        if small_index == -1 or large_index == -1:
            num = 0 # no such j 
        else: 
            num = large_index - small_index + 1
        count += num

    return count
        

def find_smallest_index(arr, value):
    n = len(arr)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= value:
            right = mid - 1
        else:
            left = mid + 1
    if left > n - 1 or arr[left] != value:
        return -1 
    else: 
        return left


def find_largest_index(arr, value):
    n = len(arr)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    if right < 0 or arr[right] != value:
        return -1 
    else: 
        return right

        
def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    arr = list(map(int(lines[1].split())))
    target = int(lines[2])
    print(count_pairs(arr, target))


if __name__ == "__main__":
    main()