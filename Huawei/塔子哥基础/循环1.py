import sys

def main():
    lines = sys.stdin.read().strip().splitlines()
    numbers = list(map(int, lines[0]))
    # left_num, right_num = numbers[0], numbers[1]
    left_weights = list(map(int, lines[1]))
    right_weights = list(map(int, lines[2]))
    if sum(left_weights) == sum(right_weights):
        print("Equal")
    else:
        print("Not Equal")


if __name__ == "__main__":
    main()