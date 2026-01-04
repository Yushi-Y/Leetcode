import sys


def traverse(edges):
    

def main():
    lines = sys.stdin.read().splitlines()
    n = int(lines[0])
    type = int(lines[1])
    if type == 1:
        edges = []
        for i in range(n):
            edge = list(map(int, lines[2+i]))
            edges.append(edge)

    if type == 2:
        edges = list(map(int, lines[2]))

    print(' '.join(traverse(edges)))


if __name__ == "__main__":
    main()
