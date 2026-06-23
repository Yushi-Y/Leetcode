import sys 
import numpy as np


def convolution(input_img, K, padding, dilation, stride, b):
    c, x, y = input_img.shape
    out, in_, k, k = K.shape
    assert c == in_  # input channels should match kernel input channels

    # dilation is like inserting zeros between kernel elements - increases the receptive field
    x_out = (x + 2*padding - dilation*(k-1) - 1)//stride + 1
    y_out = (y + 2*padding - dilation*(k-1) - 1)//stride + 1

    output = np.zeros((out, x_out, y_out))

    for o in range(out):
        for i in range(x_out):
            for j in range(y_out):
                value = 0
                for ch in range(c):
                    for m in range(k):
                        for n in range(k):
                            x_index = i * stride + m * dilation - padding
                            y_index = j * stride + n * dilation - padding
                            if 0 <= x_index < x and 0 <= y_index < y: # ensure index within bounds even with padding > 0 
                                value += input_img[ch, x_index, y_index] * K[o, ch, m, n]
                
                if b is not None:
                    value += b[o]

                output[o, i, j] = value

    return output
                        
                



def main():
    lines = sys.stdin.read().strip().splitlines()

    c, x, y = map(int, lines[0].split())

    input_img = list(map(int, lines[1].split()))
    input_img = np.array(input_img).reshape(c, x, y)

    out, in, k, k = map(int, lines[2].split())

    K = list(map(int, lines[3].split()))
    K = np.array(K).reshape(out, in, k, k)

    bias_flag, stride, padding, dilation = list(map(int, lines[4].split()))
    if bias_flag == 1:
        b = list(map(int, lines[5].split()))
        b = np.array(b)
    else:
        b = None

    output = convolution(input_img, K, padding, dilation, stride, b)
    print(' '.join(f"{v:.4f}" for v in output.flatten()))


if __name__ == "__main__":
    main()