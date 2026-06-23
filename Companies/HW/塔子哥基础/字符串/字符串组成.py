import sys

def main():
    lines = sys.stdin.read().strip().splitlines()
    str_A = lines[0]
    str_B = lines[1]
    len_A = len(str_A)
    len_B = len(str_B)

    if len_B % len_A != 0:
        print("No") 
    else:
        K = len_B // len_A
        if str_A * K == str_B:
            print("Yes") 
        else:
            print("No") 





if __name__ == "__main__":
    main()