import sys
from collections import defaultdict

def count_len(nums):
    n = len(nums)
    count = defaultdict(int) # {num: num_of_occurance}
    max_len = 0 

    left = 0

    for right in range(n):
        r = nums[right] 
        count[r] += 1
        
        while count[r] > 1: # keep updating left if there is repetition
            l = nums[left]
            count[l] -= 1
            left += 1 # push left to keep shrinking

        max_len = max(max_len, right - left + 1)

    if max_len <= n:
        return max_len
    else:    
        return -1


def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    print(count_len(nums))


if __name__ == "__main__":
    main()