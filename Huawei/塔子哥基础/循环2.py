import sys

def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    count = 0

    for i in range(1, n + 1):
        s_i = sum([int(x) for x in str(i)])
        d_i = i % 10

        if s_i % 10 == d_i:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
