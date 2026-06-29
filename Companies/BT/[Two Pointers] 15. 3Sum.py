# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that:

# i != j, i != k, j != k
# nums[i] + nums[j] + nums[k] == 0

# The solution set must not contain duplicate triplets.
# Example:
# nums = [-1, 0, 1, 2, -1, -4]
# → [[-1, -1, 2], [-1, 0, 1]]

# nums = [0, 1, 1]  →  []
# nums = [0, 0, 0]  →  [[0, 0, 0]]
# Constraints: 3 <= len(nums) <= 3000, -10^5 <= nums[i] <= 10^5.

### Thoughts
# rerank - nums
# fix nums[i] - two pointers, left and right pointer point to the rest of 2 numbers which sum to 0
# duplicate sets - remove

### pesudocode
# rank nums
# define left and right
# for i in range(n):
    # left = i + 1, right = n - 1
    # while left < right:
        # sum = num[left] + num[right] + num[i]
        # if sum == 0: add [i, left, right] into output
        # if sum < 0, left + 1
        # if sum > 0: right - 1



def sum_of_three(nums):
    # rank nums
    nums.sort()
    output = []
    n = len(nums)

    for i in range(n):
        if nums[i] == nums[i + 1]: # no need to update left as it is the same
            continue 
        left, right = i + 1, n - 1

        while left < right:
            sum = nums[left] + nums[right] + nums[i]
            if sum == 0: 
                output.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # nums[left] == nums[left + 1] - duplicate append
                # nums[right] == nums[right - 1] - duplicate append
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif sum < 0:
                left += 1
            else: # sum > 0
                right -= 1

    return output

    