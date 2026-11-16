# k[str]
# strstrstr - k times
# 3[a2[c]]
# 3[acc]
# accaccacc
# nesting - recursive - expensive
# stack - last out, first in - eliminate recurive structure in data
# pop, push - O(1) 

# 3[a2[c]]
# loop through the string
# keep every char of string (num, char, [, ]) in stack 
# stack: 3, [, a, 2, [, c, ], ]
# save it outside: 2 * c -> cc
# stack becomes: 3, [, a, cc, ]
# save it outside: 3 * acc -> accaccacc

# SC: O(n) - stack
# TC: O(n)

class Solution: 
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char) # keep adding char to stack
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr # reverse addin as we go through the stack backward

                stack.pop() # pop the left bracket

                # get the k
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * substr)

        return "".join(stack)

                

                

            
        