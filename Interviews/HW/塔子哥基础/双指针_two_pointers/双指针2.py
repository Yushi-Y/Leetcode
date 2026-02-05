import sys
from collections import defaultdict

def count_len(nums):
    n = len(nums)
    letter = defaultdict(int) # {idx: num_of_occurance}
    covered = 0 # num of covered letters
    min_len = n + 1 # a larger num to be shrinked

    left = 0

    for right in range(n):
        r = nums[right] 
        idx = ord(r) - ord('a')
        letter[idx] += 1
        if letter[idx] == 1:
            covered += 1

        while covered == 26: # keep updating left if all 26 letters exist
            min_len = min(min_len, right - left + 1) # record the length when there is still 26 letters available
            l = nums[left]
            idx_l = ord(l) - ord('a')
            letter[idx_l] -= 1
            if letter[idx_l] == 0:
                covered -= 1
            left += 1 # push left to keep shrinking

    if 0 < min_len <= n:
        return min_len
    else:    
        return -1


def main():
    lines = sys.stdin.read().strip().splitlines()
    nums = list(map(int, lines[0].split()))
    print(count_len(nums))


if __name__ == "__main__":
    main()