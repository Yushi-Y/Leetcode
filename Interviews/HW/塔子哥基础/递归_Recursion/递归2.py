import sys


def reverse(str):
    if len(str) <= 1:
        return str
    else: # n >= 2
        return reverse(str[1:]) + str[0] 



def main():
    lines = sys.stdin.read().strip().splitlines()
    str = lines[0]
    print(reverse(str))


if __name__ == "__main__":
    main()