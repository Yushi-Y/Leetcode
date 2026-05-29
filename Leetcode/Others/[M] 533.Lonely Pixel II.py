# 533. Lonely Pixel II
# Medium
# Given an m x n picture consisting of black 'B' and white 'W' pixels and an integer N, return the number of lonely black pixels.
# A black pixel at (r, c) is lonely if:

# There are exactly N black pixels in row r
# There are exactly N black pixels in column c
# Every row that has a black pixel in column c has exactly N black pixels

# Constraints:

# m == picture.length
# n == picture[i].length
# 1 <= m, n <= 500
# picture[i][j] is 'W' or 'B'
# 1 <= N <= 300

### TC: O(mn), SC: O(m+n)

def findLonelyPixel(picture, N):
    count = 0
    m, n = len(picture), len(picture[0])

    row_count = [row.count('B') for row in picture]
    col_count = [sum(picture[r][c] == 'B' for r in range(m)) for c in range(n)]

    for r in range(m):
        for c in range(n):
            if picture[r][c] == 'B' and row_count[r] == N and col_count[c] == N:
                if all(row_count[r2] == N for r2 in range(m) if picture[r2][c] == 'B'):
                    count += 1

    return count


# all(.all(...) returns True if every element in the iterable is True, False if any one of them is False.
# For example:
# pythonall([True, True, True])   # True
# all([True, False, True])  # False