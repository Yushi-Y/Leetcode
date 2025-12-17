import sys

def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    series = list(map(int, lines[1].split()))
    max_value = max(series)
    # indices = []

    indices = [index for index, value in enumerate(series) if value == max_value]
    # for i in range(n):
    #     if series[i] == max_value:
    #         indices.append(i)

    print(max_value)
    print(" ".join(map(str, indices)))


if __name__ == "__main__":
    main()