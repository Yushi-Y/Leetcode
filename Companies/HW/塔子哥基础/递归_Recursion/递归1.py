import sys

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2) # for n >= 2


def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    print(fibonacci(n))


if __name__ == "__main__":
    main()