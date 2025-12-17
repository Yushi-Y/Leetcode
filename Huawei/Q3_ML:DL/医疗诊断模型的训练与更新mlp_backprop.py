import sys
import numpy as np

def main():
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        sys.exit(0)

    L, D, K, N = map(float, lines[0].split(','))
    L, D, K = int(L), int(D), int(K)

    y_true = np.array(list(map(float, lines[1].split(',')))) # 1*K
    X = list(map(float, lines[2].split(','))) 
    W_mlp = list(map(float, lines[3].split(',')))
    W_cls = list(map(float, lines[4].split(',')))

    X = np.array(X).reshape((L, D))
    W_mlp = np.array(W_mlp).reshape((D, D))
    W_cls = np.array(W_cls).reshape((D, K))

    # Forward pass - First MLP  
    H = X @ W_mlp # L*D
    # H = np.maximum(0, H)  # ReLU activation 

    # MLP Classification 
    O = H @ W_cls  # L*K
    y_pred = O.mean(axis=0)  # Average over L samples
    
    # Loss
    mse_loss = np.mean((y_true - y_pred) ** 2) 

    # Backpropagation with chain rule
    # dL/dW_cls = dL/dy_pred * dy_pred/dO * dO/dW_cls
    # dL/dW_mlp = dL/dy_pred * dy_pred/dO * dO/dH * dH/dW_mlp
    grad_y_pred = (-2/K) * (y_true - y_pred) # (K, )
    grad_O = np.tile(grad_y_pred / L, (L, 1)) # (L, K)
    grad_W_cls = H.T @ grad_O # (D, K) = (D, L) @ (L, K) 
    grad_W_mlp = X.T @ grad_O @ W_cls.T # (D, D) = (D, L) @ (L, K) @ (K, D)

    # Gradient descents
    W_mlp_new = W_mlp - N * grad_W_mlp
    W_cls_new = W_cls - N * grad_W_cls

    print(",".join(f"{v:.2f}" for v in y_pred))
    print(f"{mse_loss:.2f}")
    print(",".join(f"{w_mlp:.2f}" for w_mlp in W_mlp_new.flatten()))
    print(",".join(f"{w_cls:.2f}" for w_cls in W_cls_new.flatten()))



if __name__ == "__main__":
    main()