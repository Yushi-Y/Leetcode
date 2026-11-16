# Problem

# You are given two sparse integer matrices:
# - mat1, with dimensions m × k.
# - mat2, with dimensions k × n.
# A sparse matrix is a matrix in which most elements are zero.

# Return their matrix product, mat1 × mat2, as a two-dimensional list of size m × n.

# Each output element is computed as:
# \[
# \text{result}[i][j] = \sum_{p=0}^{k-1} \text{mat1}[i][p]\times\text{mat2}[p][j]
# \]
# Example 1
# Input:
# mat1 = [[1, 0, 0],
#         [-1, 0, 3]]

# mat2 = [[7, 0, 0],
#         [0, 0, 0],
#         [0, 0, 1]]

# Output:
# [[7, 0, 0],
#  [-7, 0, 3]]

# Explanation:
# result[1][0] = (-1 × 7) + (0 × 0) + (3 × 0) = -7
# result[1][2] = (-1 × 0) + (0 × 0) + (3 × 1) = 3

# Example 2
# Input:
# mat1 = [[0, 2, 0]]
# mat2 = [[3, 0],
#         [0, 4],
#         [5, 0]]

# Output:
# [[0, 8]]

# Example 3
# Input:
# mat1 = [[0]]
# mat2 = [[0]]

# Output:
# [[0]]

# Assumptions for this practice version
# - 1 ≤ m, k, n ≤ 100
# - Each matrix is rectangular.
# - The number of columns in mat1 equals the number of rows in mat2.
# - All entries are integers between -100 and 100.

### pseudocode
### matrix multiplcation operations: m*n*k
# m, n, k
# initialise an empty matrix
# for i in range(m), for p in range(n), for j in range(k):
# \text{result}[i][j] = \sum_{p=0}^{k-1} \text{mat1}[i][p]\times\text{mat2}[p][j]
from typing import List

class Solution:
    def multiply(
        self,
        mat1: List[List[int]],
        mat2: List[List[int]]
    ) -> List[List[int]]:
       m, n = len(mat1), len(mat1[0])
       k = len(mat2)

       mat = [[1] * n for _ in range(m)] # m*n

       for i in range(m):
           for p in range(n):
               if mat1[i][p] != 0:
                   for j in range(k):
                       if mat2[p][j] != 0:
                           mat[i][j] += mat1[i][p] * mat2[p][j]

       return mat

# TC: O(m*n*k) - normal matrix multiplication - reduce to O(non-zero elements in mat1 * non-zero elements in mat2)
# SC: O(m*n) - store mat
        