import sys
import numpy as np



def convolution(input_img, K, stride, padding):

    C,H_in,W_in = input_img.shape
    C_k,K_h,K_w = K.shape
    assert C == C_k # Input channels should match kernel channels

    # Pad the image
    input_img = np.pad(input_img, ((0, 0), (padding, padding), (padding, padding)), 'constant', constant_values=0)

    H_out = (H_in + 2 * padding - K_h) // stride + 1
    W_out = (W_in + 2 * padding - K_w) // stride + 1

    output = np.zeros((H_out, W_out))

    for i in range(H_out):
        for j in range(W_out):
            value = 0
            for c in range(C):
                for m in range(K_h):
                    for n in range(K_w):
                        x_index = i * stride + m
                        y_index = j * stride + n
                        value += input_img[c, x_index, y_index] * K[c, m, n]
                
            output[i, j] = value

    return output



def main():
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        sys.exit(0)

    C, H_in, W_in = map(int, lines[0].split())
    C, K_h, K_w = map(int, lines[C*H_in+1].split())
    stride, padding = map(int, lines[-1].split())
    
    # read multiple lines of strings and convert to numpy array
    input_vals = []
    for i in range(1, C*H_in+1):
        input_vals.extend(map(int, lines[i].split()))
    input_img = np.array(input_vals).reshape(C, H_in, W_in)

    kernel_vals = []
    for j in range(C*H_in + 2, C*K_h + C*H_in + 2):
        kernel_vals.extend(map(int, lines[j].split()))
    K = np.array(kernel_vals).reshape(C, K_h, K_w)

    output = convolution(input_img, K, stride, padding)

    # keep the array shape, iterate each row
    for i in range(output.shape[0]):
        print(' '.join(f"{v:.4f}" for v in output[i]))
        # print(' '.join(str(int(v)) for v in output[i]))

    # print(' '.join(f"{v:.4f}") for v in output.flatten()) # flatten the array



if __name__ == "__main__":
    main()


