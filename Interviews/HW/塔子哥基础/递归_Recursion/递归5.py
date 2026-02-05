import sys

def count_path(n, x = sx, y = sy, ex, ey, k, steps):
    path_num = 0

    if x == ex and y == sy:
        path_num += 1

    if steps == k:
        return path_num

    for (dx, dy) in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        new_x = x + dx
        new_y = y + dy
        count_path(n, new_x, new_y, ex, ey, k, steps + 1)

    return path_num


def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    sx, sy, ex, ey = map(int, lines[1].split())
    k = int(lines[2])
    print(count_path(n, sx, sy, ex, ey, k))


if __name__ == "__main__":
    main()