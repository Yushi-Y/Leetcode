import sys

# f(i, j) is number of paths from (i, j) to (n-1, n-1)
# f(i, j) = f(i+1, j) + f(i, j+1)
def count_path(n, i=0, j=0):
    if n == 1:
        return 1

    if i >= n or j >= n:
        return 0

    if i == n-1 or j == n-1:
        return 1

    return count_path(n, i+1, j) + count_path(n, i, j+1)
    
    


def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    print(count_path(n))


if __name__ == "__main__":
    main()