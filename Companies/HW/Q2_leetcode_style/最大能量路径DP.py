import sys
import numpy as np



def compute_max_energy_path(img, strategy):
    H, W = img.shape
    K, _ = strategy.shape
    r = K // 2

    # Dynamic programming table to store maximum energy values
    dp = np.zeros((H, W))
    energy = np.zeros((H, W))

    max_energy = float('-inf')

    # (1) compute all energies
    for i in range(H):
        for j in range(W):
            for u in range(K):
                for v in range(K):
                    ii = i + (u - r)
                    jj = j + (v - r)
                    if 0 <= ii < H and 0 <= jj < W:
                        energy[i, j] += img[ii, jj] * strategy[u, v]  

    # (2) first column energy
    dp[:, 0] = energy[:, 0]

    # (3) DP transition
    for i in range(H):
        for j in range(W):
            # factor in margin boundaries
            candidates = [dp[i-1, j]]
            if j-1 >= 0:
                candidates.append(dp[i-1, j-1])
            if j+1 <= W-1:
                candidates.append(dp[i-1, j+1])
            dp[i, j] = max(candidates) + energy[i, j] # right, upper right, lower right

    # (4) compute max energy: take the max in the last column
    max_energy = dp[:, W-1].max() 

    return max_energy




def main():
    lines = sys.stdin.read().strip().splitlines()
    H, W, K, _ = map(int, lines[0].split())

    img = []
    strategy = []

    for i in range(1, H+1):
        lines[i] = list(map(int, lines[i].split()))
        img.append(lines[i])

    for j in range(H+2, H+K+2):
        lines[j] = list(map(int, lines[j].split()))
        strategy.append(lines[j])

    img = np.array(img)
    strategy = np.array(strategy)
    
    max_energy = compute_max_energy_path(img, strategy)

    print(f"{max_energy:.1f}")



if __name__ == "__main__":
    main()