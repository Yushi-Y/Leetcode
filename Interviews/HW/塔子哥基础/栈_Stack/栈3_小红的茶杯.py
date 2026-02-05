import sys

def solve(numbers):
    stack = []
    x = len(numbers)

    for num in numbers:
        stack.append(num)

    # apply two rules
    changes = True
    while len(stack) >= 2 and changes:
        changes = False

        if stack[-1] == stack[-2]:
            top = stack[-1]
            stack.pop()
            stack.pop()
            stack.append(top * 2)
            changes = True
            continue # go back to the while loop to check again on new stack

        max_y = min(x, len(stack) - 1) # y elements apart from the top
        for y in range(1, max_y + 1):
            total = sum(stack[-(y + 1):-1]) # sum of the y elements below the top

            if stack[-1] == total:
                sum = total + stack[-1]
                for i in range(y + 1):
                    stack.pop()
                stack.append(sum)

                changes = True
                break # break the for loop and start from while to check smaller y

    return stack


def main():
    numbers = list(map(int, input().strip().split()))
    stack = solve(numbers)
    print(' '.join(map(str, stack)))


if __name__ == "__main__":
    main()