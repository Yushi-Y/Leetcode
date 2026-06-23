import sys

def main():
    lines = sys.stdin.strip().splitlines()
    for line in lines:
        line = list(map(int, line))
        total = sum(line)
        print(total)


# def main():
#     while True:
#         try: 
#             line = list(map(int,input().strip()))
#             total = sum(line)
#             print(total)
#         except EOFError:
#             break


if __name__ == "__main__":
    main()