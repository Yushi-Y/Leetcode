import sys

# nums is a sorted array
def twoSum(nums, target):
    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
        if nums[left] + nums[right] == target:
            return [left + 1, right + 1]
        
        elif nums[left] + nums[right] < target:
            left += 1

        else:
            right -= 1

    return -1



def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    target = int(lines[2])
    print(' '. join(map(str, twoSum(nums, target))))


if __name__ == "__main__":
    main()