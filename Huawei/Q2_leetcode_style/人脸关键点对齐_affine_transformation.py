import sys

def affine_transformation(A:list, M:list) -> list:
    H = len(A)
    W = len(A[0])

    a, b, t_x = M[0]
    c, d, t_y = M[1]
    det = a * d - b * c
    if det == 0:
        raise ValueError("The matrix is not invertible.")

    transformed_list = [[0 for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            x_new = 1/det * (d*(i-t_x) - b*(j-t_y))
            y_new = 1/det * (-c*(i-t_x) + a*(j-t_y))

            x_round = round(x_new)
            y_round = round(y_new)
            if 0 <= x_round <= H and 0 <= y_round <= W:
                transformed_list[i][j] = A[x_round][y_round]
            else:
                transformed_list[i][j] = 0

    transformed_list = [v for row in transformed_list for v in row]

    return transformed_list



if __name__ == "__main__":
    lines = sys.stdin.read().strip().splitlines()

    if not lines:
        sys.exit(0)

    a, m, _ = map(int, lines[0].split())
    A = list(map(int, lines[i + 1].split() for i in range(a)))
    M = list(map(int, line[i + a + 1].split() for i in range(m)))

    transformed_list = affine_transformation(A,M)

    print(transformed_list)

