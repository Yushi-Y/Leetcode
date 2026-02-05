import sys
import numpy as np


def convolution(c_in, x, y, input_data, k_out, k_in, k, weights, b, stride, padding, dilation):
    # define output size
    c_out = k_out
    x_out = ((x + 2 * padding - dilation * (k-1) -1)//stride + 1)
    y_out = ((y + 2 * padding - dilation * (k-1) -1)//stride + 1)

    output_data = np.zeros((c_out, x_out, y_out))

    weights = np.array(weights).reshape((c_out, k_in, k, k))
    input_data = np.array(input_data).reshape((c_in, x, y))

    for c in range(c_out):
            for i in range(x_out):
                for j in range(y_out):
                    s = 0
                    for d in range(c_in):
                        for u in range(k):
                            for v in range(k):
                                input_x = i*stride + u*dilation - padding
                                input_y = j*stride + v*dilation - padding
                                if 0 <= input_x < x and 0 <= input_y < y:
                                    s += weights[c, d, u, v]*input_data[d, input_x, input_y] 
                                
                    if b is not None:
                        s += b[c]

                    output_data[c, i, j] += s

    return output_data.flatten().tolist()



def main():
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        sys.exit(0)

    c_in,x,y = map(int, lines[0].split()) # input_channel, input_width, input_height
    input_data = list(map(float, lines[1].split()))
    k_out,k_in,k = map(int, lines[2].split()[::-1]) # kernel_output_channel, kernel_input_channel, kernel_size
    weights = list(map(float, lines[3].split()))
    bias_flag,stride,padding,dilation = map(int, lines[4].split())

    if bias_flag == 1:
        b = list(map(float, lines[5].split()))
    else:
        b = None


    output = convolution(c_in, x, y, input_data, k_out, k_in, k, weights, b, stride, padding, dilation)

    print(output)
    


if __name__ == "__main__":
    main()