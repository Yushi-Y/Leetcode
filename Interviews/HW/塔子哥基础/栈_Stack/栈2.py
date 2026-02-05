import sys

# use a stack to process the array from left and pop three consecutive characters

def remove_duplicates(arr):
    stack = [] # keep a separate list from the array
    i = 0

    for num in arr:
        stack.append(num)
        while len(stack) >= 3 and stack[-1] == stack[-2] == stack[-3]:
            stack.pop()
            stack.pop()
            stack.pop()

    return stack


def main():
    arr = list(map(int, input().strip().split()))
    new_arr = remove_duplicates(arr)
    if new_arr:
        print(' '.join(map(str, new_arr)))
    else:
        print(' ')

if __name__ == "__main__":
    main()