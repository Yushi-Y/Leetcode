import sys

def query(nums, query_tuples):
    positions = []

    # create an index map of positions: {num1:[1,3,5,7]; num2:[2,4,6]}
    index_map = {}
    for i, num in enumerate(nums):
        if num not in index_map:
            index_map[num] = []
        index_map[num].append(i)
        # index_map[num] = index_map.setdefault(num, []).append(i)
        # .setdefault() returns the list compared to .get() that returns None, as .append modifies the list in-place and returns None

    for (q, k) in query_tuples:
        position = -1 # if not find, return -1

        all_positions = index_map.get(q, [])
        if k <= len(all_positions):
            position = all_positions[k - 1]

        positions.append(position)

    return positions


def main():
    lines = sys.stdin.read().strip().splitlines()
    n, Q = map(int, lines[0].split())
    nums = list(map(int, lines[1].split()))

    query_tuples = []
    for i in range(Q):
        q, k = map(int, lines[2 + i].split())
        query_tuples.append((q, k))

    results = query(nums, query_tuples)
    print('\n'.join(map(str, results))) # one answer per line


if __name__ == "__main__":
    main()



# import sys

# def query(nums, query_tuples):
#     positions = []

#     for (x, k) in query_tuples:
#         query_times = 0
#         position = -1 # if not find, return -1

#         for i, num in enumerate(nums):
#             if num == x:
#                 query_times += 1
#                 if query_times == k:
#                     position = i
#                     break

#         positions.append(position)

#     return positions


# def main():
#     lines = sys.stdin.read().strip().splitlines()
#     n, Q = map(int, lines[0].split())
#     nums = list(map(int, lines[1].split()))

#     query_tuples = []
#     for i in range(Q):
#         x, k = map(int, lines[2 + i].split())
#         query_tuples.append((x, k))

#     results = query(nums, query_tuples)
#     print('\n'.join(map(str, results))) # one answer per line


# if __name__ == "__main__":
#     main()