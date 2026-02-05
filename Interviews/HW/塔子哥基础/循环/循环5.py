import sys
import numpy as np

# TC is O(q * r * c) where r = x2-x1+1 and c = y2-y1+1
def main():
    lines = sys.stdin.read().strip().splitlines()
    n, m = map(int, lines[0].split())

    matrix = [list(map(int, lines[1:i+1])) for i in range(1, n + 1)]
    matrix = np.array(matrix).reshape(n, m)

    q = int(lines[n+1])
    queries = [list(map(int, lines[n+2:n+2+j])) for j in range(1, q + 1)]
    queries = np.array(queries).reshape(q, 4)

    list_max_value = []

    for row in queries: # [x1, y1, x2, y2]
        x1, y1, x2, y2 = row
        max_value = -float("inf")
        for i in range(x1 - 1, x2): # make 0-index
            for j in range(y2 - 1, y2):
                max_value = max(max_value, matrix[i, j])

        list_max_value.append(max_value)

    for max_val in list_max_value:
        print(max_val)

if __name__ == "__main__":
    main()