import sys

# time complexity: O(q * k), q is number of queries and k = r - l + 1

def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    q = int(lines[2])

    for i in range(1, q + 1):
        l, r = list(map(int, lines[2 + i].split()))
        left, right = l - 1, r - 1
    
        max_value = arr[left] # python slicing is also right-exclusive
        indices = []

        for idx in range(left, right + 1):
            if arr[idx] > max_value:
                max_value = arr[idx]   # start fresh with new max, discard previous max indices 
                indices = [idx + 1]
            elif arr[idx] == max_value:
                indices.append(idx + 1)

        # indices = [index for index, value in enumerate(arr) if value == max_value]
        # indices = [idx + 1 for idx in indices if left <= idx <= right]

        print(max_value)
        print(' '.join(map(str, indices)))

if __name__ == "__main__":
    main()