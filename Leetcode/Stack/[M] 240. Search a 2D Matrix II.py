# Start from the top-right corner. At each step you can eliminate an entire row or column:
# Current value too big → move left
# Current value too small → move down

# This gives you O(m + n) time, SC O(1) as just checking 'row' and 'col' numbers


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        row = 0
        col = n - 1 # 0-indexed


        while row < m and col >= 0: # boundary fit with moving direction
            entry = matrix[row][col]

            if target == entry:
                return True
            elif target < entry:
                col -= 1
            else:
                row += 1

        return False

            