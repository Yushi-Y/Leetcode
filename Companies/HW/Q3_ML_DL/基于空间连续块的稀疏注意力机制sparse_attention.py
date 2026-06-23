import sys
import math
import numpy as np


def sparse_attention(n, b, d, X, W_1, W_2, b_1, b_2):
    A = []
    m = math.ceil(n/b)

    for j in range(m):
        h = np.mean(X[j*b:min((j+1)*b,n)],axis=0) # (d,)
        middle = max(0, float(W_1 @ h + b_1)) # scalar
        c = W_2 * middle + b_2 # (d,)
        a = float(c.sum())/math.sqrt(d) # scalar
        A.append(a) # m*1


    # Compute S: best split maximizing min(left_sum, right_sum) - loop through all split indexes once - greedy algorithm (local best = global best), TC O(m)
    S = -1e5
    total = sum(A)
    left_sum = 0

    for i in range(1,m): # both sides must be non-empty
        left_sum += A[i-1]
        S = max(S, min(left_sum, total-left_sum))

    return round(100*S)



def main():
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        sys.exit(0)
    
    X = []

    n, d, b = map(int,lines[0].split())

    for i in range(1, n+1):
        x_i = np.array(list(map(float,lines[i].split())))
        X.append(x_i)

    X = np.array(X)
    W_1 = np.array(list(map(float,lines[-2].split()))) # (d,)
    W_2 = np.array(list(map(float,lines[-1].split()))) # (d,)
    b_1, b_2 = 2.0, 1.0

    output = sparse_attention(n, b, d, X, W_1, W_2, b_1, b_2)

    print(output)


    
if __name__ == "__main__":
    main()