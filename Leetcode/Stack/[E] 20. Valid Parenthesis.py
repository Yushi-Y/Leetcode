# Use stack to track all brackets
# loop through s, if s is open, push it to stack
# if it closed, check if stack top matches of open matches it, if not, return False
# at the end stack should be empty, if not, return False

# TC: O(n)
# SC: O(n) - one stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in map.values(): # open
                stack.append(char)
            else: # closed
                if not stack or stack[-1] != map[char]: # no open brackets in stack or no match
                    return False
                stack.pop() # pop the last open bracket as matched
        return stack == [] # true if stack is empty

        
        