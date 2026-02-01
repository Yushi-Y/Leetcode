# Compute the rating level after adding changes
def compute_rating_level(initial_rating, changes):
    rating = initial_rating
    
    for change in changes:
        rating += change
        
    if rating < 1000:
        return "beginner"
    
    elif rating < 1500:
        return "intermediate"
    
    elif rating < 2000:
        return "advanced"
    
    else:
        return "pro"



# Drop Bubbles Game
def pop_bubbles(bubbles, operations):
    m, n = len(bubbles), len(bubbles[0])

    # Check whether a given cell is within the boundaries of the board
    def is_valid(i, j):
        return 0 <= i < m and 0 <= j < n

    # Return a list of adjacent cells to a given cell
    def get_adjacent_cells(i, j):
        return [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

    # Recursively remove bubbles of the same color and return the number of bubbles removed
    def remove_bubbles(i, j, color):
        if bubbles[i][j] != color:
            return False
        
        bubbles[i][j] = 0
        removed = 1
        
        for r, c in get_adjacent_cells(i, j):
            if is_valid(r, c) and bubbles[r][c] == color:
                removed += remove_bubbles(r, c, color)
                
        return removed

    # Drop remaining bubbles in cells above the empty cells
    def drop_bubbles(bubbles):
        rows = len(bubbles)
        cols = len(bubbles[0])
    
        for j in range(cols):
            stack = []
            for i in range(rows):
                if bubbles[i][j] != 0:
                    stack.append(bubbles[i][j])
                    bubbles[i][j] = 0
        
            k = rows - 1
            while stack:
                if bubbles[k][j] == 0:
                    # Drop the bubble by popping a bubble off the end of the stack and place it in the empty cell
                    bubbles[k][j] = stack.pop()
                else:
                    # If the cell already contains a bubble, move down a row to the next empty cell
                    k -= 1
                    
    # If the clicked cell is empty, moves on to the next turn
    for i, j in operations:
        if bubbles[i][j] == 0:
            continue

        # Otherwise, remove all bubbles of the same color
        color = bubbles[i][j]
        removed = remove_bubbles(i, j, color)

        # If less than 2 bubbles were removed, the clicked cell is restored to its original color
        if removed < 2:
            bubbles[i][j] = color
        drop_bubbles()
    
    return bubbles



# Find the maximum prefix length of two numbers
def longest_common_prefix_length(first_array, second_array):
    
    # Initialize the maximum prefix length to 0
    max_prefix_len = 0
    
    # Iterate over all pairs of numbers from different arrays
    for num1 in first_array:
        for num2 in second_array:
            # Convert the numbers to strings
            str1 = str(num1)
            str2 = str(num2)
            
            # Find the common prefix length
            prefix_len = 0
            while prefix_len < len(str1) and prefix_len < len(str2) and str1[prefix_len] == str2[prefix_len]:
                prefix_len += 1
            
            # Update the maximum prefix length for this pair of number
            max_prefix_len = max(max_prefix_len, prefix_len)
    
    # Return the overall maximum prefix length
    return max_prefix_len
