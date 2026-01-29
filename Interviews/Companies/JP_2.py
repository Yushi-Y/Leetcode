import math

def euclidean_distance(a: list[float], b: list[float]) -> float:
    if not a or not b:
        raise ValueError("It's empty or None")
    
    if len(a) != len(b):
        raise ValueError("Unequal length so cannot compare")

    squared_sum = [sum((x - y)**2) for x, y in zip(a, b)]
    dist = math.sqrt(squared_sum)

    return dist


def most_frequent(x: list[int]) -> int:
    """Return the most frequent number in x.
    """
    ...
    return max(set(x), key=x.count)


def knn_classify(
  X: list[list[int]],
  y: list[int],
  new_x: list[int],
  k: int = 3
) -> int:
    """
    Classifies new_point using k-Nearest Neighbors.

    Parameters:
        X: Existing points, shape (num_of_points, space_dim)
        y: Labels for existing points, shape (num_of_points,)
        new_point: The new point to classify, shape (space_dim,)
        k: Number of neighbors to use

    Example:

    X = [
        [1, 2, 3, 4], # label 0
        [2, 3, 4, 5], # label 0
        [9, 8, 7, 6], # label 1
        [8, 7, 6, 5], # label 1
        [1, 2, 2, 3]  # label 0
    ]

    y = [0, 0, 1, 1, 0]

    new_point = [1, 2, 3, 3]

    expected label: 0
    """
    # new point is empty/none
    # y outside of [0, 1]
    # X vectors do not make sense geometrically with its labels
    # dimensions of X and new_point does not match

    distance_and_label = []

    for x_i, label in zip(X, y):
        dist = euclidean_distance(x_i, new_x)
        distance_and_label.append([dist, label])

    distance_and_label.sort(distance_and_label, key = lambda x:x[0]) #[[dist, label], ...]

    k_labels = [label for _, label in distance_and_label[:k]]

    return most_frequent(k_labels)

    # SC: O(n), n is num of elements in X
    # TC: euclidean dist is O(d) where d is dimension of a vector in X, binary sort is O(nlogn)
    # when n >> d, O(nlogn) dominates
