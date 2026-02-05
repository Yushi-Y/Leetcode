import sys


def exists(arr, q):
    n = len(arr)

    left, right = 0, n - 1 
    while left <= right: # break if left > right
        mid = (left + right) // 2 # middle index
        if arr[mid] == q:
            return True
        elif arr[mid] < q:
            left = mid + 1
        else: # arr[mid] > q:
            right = mid - 1
    return False


def query_found(arr, queries)
    return ["YES" if exists(arr, q) else "NO" for q in queries]

# def query_binary_search(arr, queries):
#     n = len(arr)
#     results = []

#     for q in queries:
#         left, right = 0, n - 1 # re-initialise left and right indexes for each query
#         while left <= right: # break if left > right
#             mid = (left + right) // 2 # middle index
#             if arr[mid] == q:
#                 results.append("YES")
#                 break
#             elif arr[mid] < q:
#                 left = mid + 1
#             else: # arr[mid] > q:
#                 right = mid - 1
#         else: # if append yes from while loop, then do not go here
#             results.append("NO")

#     return results


def main():
    lines = sys.stdin.read().strip().splitlines()

    n, Q = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))

    queries = []
    for i in range(Q):
        queries.append(int(lines[2 + i]))

    results = query_found(arr, queries)
    print('\n'.join(results))


if __name__ == "__main__":
    main()