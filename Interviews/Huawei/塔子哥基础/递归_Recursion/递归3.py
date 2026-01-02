import sys


def max_sum(arr, index=0): # always start from root node
    n = len(arr)

    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index >= n: # left node not exist, then it is a leaf node
        return arr[index]

    left_sum = max_sum(left_index)

    if right_index < n: # right node exists
        right_sum = max_sum(right_index)
        return max(left_sum, right_sum) + arr[index] # add current node value too
    else:
        return left_sum + arr[index]


def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    print(max_sum(arr))


if __name__ == "__main__":
    main()