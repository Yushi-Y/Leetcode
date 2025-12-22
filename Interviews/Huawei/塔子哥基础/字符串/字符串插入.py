import sys


def main():
    lines = sys.stdin.read().strip().splitlines()
    A = lines[0]
    B = lines[1]

    for i in range(len(A) + 1):
        new_string = A[:i] + B + A[i:]
        if new_string == new_string[::-1]:
            print("YES")
        else:
            print("NO")
        


if __name__ == "__main__":
    main()