# Binary search to narrow down space O(logn)

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n-1][n-1]
        
        while left < right:
            mid = (left + right) // 2 # mid matrix value
            count = self.count_less_than_target(matrix, mid)
            
            if count < k:
                left = mid + 1
            else:
                right = mid

        return left


    def count_less_than_target(self, matrix, target):
        """Count the number of elements less than target in the matrix. Start from top right corner to speed up counting. """
        # start from top right corner
        n = len(matrix)
        count = 0

        row = 0
        col = n - 1

        while row < n and col >= 0:
            if matrix[row][col] <= target:
                count += col + 1 # shift from 0-index
                row += 1
            else:
                col -= 1

        return count



### TC
# Binary search on value range: O(log(max - min))

# left = matrix[0][0] (minimum value)
# right = matrix[n-1][n-1] (maximum value)
# Search space = max - min
# Binary search iterations = log(max - min)


# Count operation per iteration: O(n)

# Starting from top-right corner (row=0, col=n-1)
# Each step: either move down (row++) or move left (col--)
# Maximum moves = n rows + n columns = 2n
# But we can only make n row moves and n column moves total
# Worst case: traverse entire diagonal-like path = O(n)


# Total: O(n × log(max - min))


### SC
# Variables only:

# left, right, mid → O(1)
# count, row, col, n → O(1)
# No additional data structures

# No recursion: Iterative approach, constant stack space
# In-place: No modification to input matrix