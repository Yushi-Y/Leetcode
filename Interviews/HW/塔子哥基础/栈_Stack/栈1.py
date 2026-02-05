import sys

def main():
    s = input().strip()

    # maintain count with order
    count = 0
    for char in s:
        if char == "(":
            count += 1
        else:
            count -= 1
        
    print("YES" if count == 0 else "NO")


if __name__ == "__main__":
    main()