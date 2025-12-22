import sys

def query(nums, query_nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) += 1
    
    results = []
    for query in query_nums:
        query_times = freq.get(query, 0)
        results.append(query_times)

    return results


def main():
    lines = sys.stdin.read().strip().splitlines()
    n, Q = map(int, lines[0].split())
    nums = list(map(int, lines[1].split()))

    query_nums = []
    for i in range(Q):
        q = int(lines[2 + i])
        query_nums.append(q)

    results = query(nums, query_nums)
    print('\n'.join(map(str, results))) 
    # one answer per line


if __name__ == "__main__":
    main()



# import sys

# def query(nums, query_nums):
#     results = []

#     for q in query_nums:
#         query_times = 0

#         for num in nums:
#             if num == q,
#             query_times += 1

#         results.append(query_times)

#     return results


# def main():
#     lines = sys.stdin.read().strip().splitlines()
#     n, Q = map(int, lines[0].split())
#     nums = list(map(int, lines[1].split()))

#     query_nums = []
#     for i in range(Q):
#         q = int(lines[2 + i])
#         query_nums.append(q)

#     results = query(nums, query_nums)
#     print('\n'.join(map(str, results))) 
#     # one answer per line


# if __name__ == "__main__":
#     main()