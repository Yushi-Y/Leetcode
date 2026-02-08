# algo: monotonic stack

# This is a monotonic stack problem (specifically a decreasing stack).
# Hint: maintain a stack of indices where temperatures are in decreasing order. For each new temperature:

# Code logic:
# While the stack is non-empty and the current temp is warmer than the temp at the stack's top index → pop and compute the difference in indices
# Push the current index onto the stack


# Let's walk through temps = [73, 74, 75, 71, 69, 72, 76, 73]
# stack = []  (stores indices)
# answer = [0, 0, 0, 0, 0, 0, 0, 0]

# i=0, temp=73 → stack empty, push 0        stack: [0]
# i=1, temp=74 → 74 > 73 (top), pop 0       answer[0] = 1-0 = 1
#                push 1                      stack: [1]
# i=2, temp=75 → 75 > 74 (top), pop 1       answer[1] = 2-1 = 1
#                push 2                      stack: [2]
# i=3, temp=71 → 71 < 75 (top), just push   stack: [2, 3]
# i=4, temp=69 → 69 < 71 (top), just push   stack: [2, 3, 4]
# i=5, temp=72 → 72 > 69 (top), pop 4       answer[4] = 5-4 = 1
#                72 > 71 (top), pop 3        answer[3] = 5-3 = 2
#                72 < 75 (top), stop & push  stack: [2, 5]
# i=6, temp=76 → 76 > 72 (top), pop 5       answer[5] = 6-5 = 1
#                76 > 75 (top), pop 2        answer[2] = 6-2 = 4
#                push 6                      stack: [6]
# i=7, temp=73 → 73 < 76 (top), just push   stack: [6, 7]

# Remaining in stack (6, 7) → no warmer day → stay 0

# answer = [1, 1, 4, 2, 1, 1, 0, 0] ✓

# The key idea: the stack holds indices of days still "waiting" for a warmer day. When a warmer day arrives, we pop and calculate the gap.


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answer = [0] * n

        for i in range(n):
            # while not if — one new temperature can resolve multiple waiting days
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx # compute the gap
            stack.append(i)

        return answer




        