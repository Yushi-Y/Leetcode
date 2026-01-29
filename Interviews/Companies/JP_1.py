# find the start and end of a line in a binary 2D matrix
# You have a 2D array (matrix) of 0s and 1s.
# 1 represents the stroke; 0 is background.
# Stroke is either horizontal or vertical, but you don’t know where it is.
# Goal: find the start and end coordinates of the stroke.


# TC O(R*C) - as two for loops in either horizontal or vertical
# SC O(R) or O(C) - One array stored for either horizontal or vertical
def find_stroke_endpoints(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # horizontal stroke
    for i in range(rows):
        row_indices =  [j for j in range(cols) if matrix[i][j] == 1]
        if row_indices: 
            start = (i, row_indices[0])
            end = (i, row_indices[-1])

    # vertical stroke
    for j in range(cols):
        col_indices =  [i for i in range(rows) if matrix[i][j] == 1]
        if col_indices: 
            start = (col_indices[0], j)
            end = (col_indices[-1], j)

    return start, end



# now i know that the length of stroke is definitely > half of paper
# can optimise the solution by searching from the middle point
# If a horizontal stroke is longer than cols/2, checking ANY column will hit it
# Similarly, if a vertical stroke is longer than rows/2, checking ANY row will hit it

# TC O(R+C)
# SC O(1) - No arrays, lists, or data structures created
def find_stroke_endpoints_fast(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    mid_row = rows // 2
    mid_col = cols // 2

    # horizontal stroke
    for i in range(rows):
        if matrix[i][mid_col] == 1:
            start_col = -1
            for j in range(cols):
                if matrix[i][j] == 1:
                    start_col = j
                    break

            end_col = -1
            for j in range(cols-1, -1, -1): # zero-indexed
                if matrix[i][j] == 1:
                    end_col = j
                    break

            start = (i, start_col)
            end = (i, end_col)

            if start_col != end_col:
                return start, end # return immediately to avoid vertical check


    # vertical stroke
    for j in range(cols):
        if matrix[mid_row][j] == 1:
            start_row = -1
            for i in range(rows):
                if matrix[i][j] == 1:
                    start_row = i
                    break

            end_row = -1
            for i in range(rows-1, -1, -1): # zero-indexed
                if matrix[i][j] == 1:
                    end_row = i
                    break

        start = (start_row, j)
        end = (start_row, j)

        if start_row != end_row:
            return start, end
    
    return None, None



