# Given an m x n picture consisting of black 'B' and white 'W' pixels, return the number of lonely black pixels.
# A black pixel is lonely if it is the only black pixel in its entire row and the entire column it belongs to.
# Example 1:
# Input: picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
# Output: 3
# Explanation: All three 'B's are lonely pixels.
# Example 2:
# Input: picture = [["B","B","B"],["B","B","B"],["B","B","B"]]
# Output: 0
# Constraints:

# m == picture.length
# n == picture[i].length
# 1 <= m, n <= 500
# picture[i][j] is 'W' or 'B'


#### TC: O(mn)
#### SC: O(m + n)

def findLonelyPixel(picture):
    count = 0
    m, n = len(picture), len(picture[0])

    # for each row, compute number of 'B' in each row
    # for each col, compute number of 'B' in each col
    row_count = [row.count('B') for row in picture] # count is a method for list
    col_count = [sum(picture[r][c] == 'B' for r in range(m)) for c in range(n)]

    # scan every cell, for every black cell, check exactly one black on this row and col
    for r in range(m):
        for c in range(n):
            if picture[r][c] == 'B' and row_count[r] == 1 and col_count[c] == 1:
                count += 1

    return count

