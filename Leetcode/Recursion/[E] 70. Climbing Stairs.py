# Hint 1 – Recursive Thinking
# If you're standing on step n, how did you get there? You either came from step n-1 (took 1 step) or step n-2 (took 2 steps). So the number of ways to reach step n is...?

# Hint 2 – The Recurrence
# ways(n) = ways(n-1) + ways(n-2). Does this formula remind you of anything famous?

# Hint 3 – Base Cases
# You need two base cases to anchor the recursion. How many ways are there to climb 1 step? How many ways for 2 steps? 

# Hint 4 – Why Pure Recursion is Too Slow
# If you just do naive recursion, you recompute the same subproblems over and over (e.g., ways(3) gets called many times). The time complexity explodes to O(2^n). You can fix this with either memoization (top-down) or a simple loop (bottom-up). For this problem, the bottom-up approach only needs two variables — no array required.

#### Key takeaway: This is essentially the Fibonacci sequence. In interviews, showing that you can go from naive recursion → memoization → optimized iterative solution demonstrates strong DP understanding. 
# The optimal version only tracks the two previous values since that's all the recurrence needs.



### Bottom-up DP with two variables
# TC O(n), SC O(1)
# Only keep track of last two variables, so space is O(1)
class Solution:
    def climbStairs(self, n: int, memory = {}) -> int:
        if n <= 2:
            return n
        prev_2, prev_1 = 1, 2

        for i in range(3, n + 1):
            current = prev_1 + prev_2
            prev_1 = current
            prev_2 = prev_1

        return prev_1


### Recursion with Memorisation (Top-down DP)
# TC O(n), SC O(n)
# The key insight: when n is not in memory, we don't give up — we recurse deeper. That recursion keeps going until it hits either a base case (n <= 2) or something already stored. So by the time we actually compute memory[n], the subproblems n-1 and n-2 are guaranteed to already be solved.

# It's impossible to miss a previous element because the recursion won't let you compute f(5) until f(4) and f(3) are done, and f(4) won't finish until f(3) and f(2) are done, and so on all the way down to the base cases.

# class Solution:
#     def climbStairs(self, n: int, memory = {}) -> int:
#         if n <= 2:
#             return n
#         if n in memory:
#             return memory[n] # In memory → we return immediately (O(1) lookup), no recursion needed

#         memory[n] = self.climbStairs(n - 1, memory) + self.climbStairs(n - 2, memory)

#         return memory[n]



### Naive recusion: TC (O(2^))
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2

#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# Each call makes **two** more calls. Draw the call tree for n=5:
# ```
#                     f(5)
#                 /          \
#             f(4)            f(3)
#            /    \          /    \
#         f(3)    f(2)    f(2)    f(1)
#        /    \
#     f(2)    f(1)

# At every level, the number of calls roughly doubles. The tree has about n levels deep, so the total number of calls is roughly 2 × 2 × 2 × ... (n times) = 2^n.
        