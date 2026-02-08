# Monotonic stack, similar to Q709

# 'Circular' means after the last element, you wrap back to the beginning. Think of the array as a loop:

# nums = [1, 2, 3, 4, 3]
# Linear:    1 → 2 → 3 → 4 → 3 → end
# Circular:  1 → 2 → 3 → 4 → 3 → 1 → 2 → 3 → 4 → 3 → ...

# Hint: iterate through the array twice (i.e., range(2 * n)) and use i % n to wrap around. This simulates the circular traversal.

# i=0 → 0 % 5 = 0
# i=1 → 1 % 5 = 1
# i=2 → 2 % 5 = 2
# i=3 → 3 % 5 = 3
# i=4 → 4 % 5 = 4
# i=5 → 5 % 5 = 0  ← wraps back
# i=6 → 6 % 5 = 1
# i=7 → 7 % 5 = 2
# i=8 → 8 % 5 = 3
# i=9 → 9 % 5 = 4
# So it cycles through 0, 1, 2, 3, 4, 0, 1, 2, 3, 4 — exactly simulating the circular array.

# Code logic
# While the stack is non-empty and the current num is larger than the num at the stack's top index → pop and add the current num to answers
# Push the current index onto the stack

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        answers = [-1] * n
 
        for i in range(n * 2):
            idx = i % n
            while stack and nums[idx] > nums[stack[-1]]:
                last = stack.pop()
                answers[last] = nums[idx]
            if i < n:
                stack.append(idx) 

        return answers

            

        