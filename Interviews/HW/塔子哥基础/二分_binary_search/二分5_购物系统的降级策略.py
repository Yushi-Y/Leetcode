import sys

# create a new array of sums at different values = 1, 2, ... and do binary search in the sum array
# then value is just the arr index that is the largest <= cnt (二分3)
def compute_value(arr, max_value):
    if sum(arr) <= max_value:
        return -1
    
    left, right = 0, max(arr)

    while left <= right:
        mid = (left + right) // 2
        sum_value = sum([min(i, mid) for i in arr])

        if sum_value > max_value:
            right = mid - 1
        else:
            left = mid + 1

    return max(0, right)


# def compute_value(arr, max_value):
#     n = len(arr)
#     sum_arr = []
#     M = max(arr)

#     if sum(arr) <= max_value:
#         return -1
#     # elif n > max_value:
#     #     return 0
#     
    #  for val in range(0, M + 1):
    #      sum_value = sum([min(i, val) for i in arr])
    #      sum_arr.append(sum_value)

#     index = find_largest_index(sum_arr, max_value)
#     return index


# def find_largest_index(arr, max_value):
#     n = len(arr)
#     left, right = 0, n - 1

#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] > max_value:
#             right = mid - 1
#         else:
#             left = mid + 1

#     return max(0, right)
#     # if right < 0:
#     #     return 0
#     # else: 
#     #     return right


def main():
    lines = sys.stdin.read().strip().splitlines()
    arr = list(map(int, lines[0].split()))
    max_value = int(lines[1])
    print(compute_value(arr, max_value))


if __name__ == "__main__":
    main()