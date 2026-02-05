"""
Problem: Select K Random Elements from a List

Given a list of elements and an integer k, return k unique elements 
selected uniformly at random from the list.

Constraints:
- If k >= len(list), return all elements
- Each element should have equal probability of being selected
- Elements should be unique (no duplicates from selection process)

Example:
    Input:  l = [1, 2, 3, 4, 5], k = 3
    Output: [3, 1, 5]  (any 3 unique elements)
"""

import random


# Approach 1: Using built-in random.sample
def find_elements_v1(l: list, k: int) -> list:
    """Select k random unique elements using random.sample."""
    n = len(l)
    if k >= n:
        return l
    return random.sample(l, k)


# Approach 2: Shuffling 
# TC: O(n), SC: O(n)
def find_elements_v2(l: list, k: int) -> list:
    """Select k random unique elements via partial shuffle."""
    n = len(l)
    if k >= n:
        return l.copy()
    
    l = l.copy()  # avoid mutating original
    for i in range(n):  # shuffle everything
        j = random.randint(i, n - 1)
        l[i], l[j] = l[j], l[i]
    return l[:k]


# Approach 3: if k << n, try to save TC
# TC: O(k), SC: O(1)
def find_elements_v3(l: list, k: int) -> list:
    """Select k random unique elements via partial shuffle."""
    n = len(l)
    
    for i in range(k):  # only need k swaps
        j = random.randint(i, n - 1)
        l[i], l[j] = l[j], l[i]
    return l[:k]