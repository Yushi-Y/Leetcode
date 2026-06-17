# 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in sorted order, not the kth distinct element.
# Can you solve it without sorting? (That last line is the real challenge the problem is hinting at.)
# Example:

# nums = [3,2,1,5,6,4], k = 2 → output 5
# nums = [3,2,3,1,2,4,5,5,6], k = 4 → output 4

# Constraints: 1 <= k <= nums.length <= 10^5, -10^4 <= nums[i] <= 10^4.


### Thoughts: heap (堆) - priority queue
# initialise a heap wit size k
# for num in nums: add num to heap
# if heap size > k, push element out of heap
# return heap top - k-th largest element

### TC: O(n*logk) - n in for loop, log k for inserting element to heap with size k
### SC: O(k), heap size is k

import heapq

def findKthLargest(self, nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap) # pop the smallest

    return heap[0] # heap top is largest

    