# split the string into 4 parts, all valid (between 0 - 255, no leading zero unless only '0')
# try all possible splits with backtracking - recursively find all possible solutions, if one path of solution does not work, go back to last step ('undo' a step) on the path
# at each step, make a choice by picking 1-3 digits as a segment
# if this choice leads to a valid path, continue recursively
# otherwise, undo this choice and try another
# this way we try all combinations

# TC: O(1)
# SC: O(1)
# Everything is bounded by the fixed structure of an IP address (always 4 segments), so no space scales with input size.
# "Both time and space are O(1) because the input length is bounded to 12 characters and recursion depth is fixed at 4."

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        result = []

        def is_valid(segment): # a string
            # if seg starts with 0 and len > 1, false
            # if int > 255, false
            if segment[0] == '0' and len(segment) > 1:
                return False
            return 0 <= int(segment) <= 255

        # start is your current position (index) in the string — it tracks how far you've consumed characters.
        # Every time you pick a segment of length, you advance: start + length
        # segments is ['1', '0', '10', '23'] - list of current segments
        def backtrack(start, segments):
            # only pass case: assume all segments there and all chars consumed
            if len(segments) == 4 and start == len(s):
                result.append('.'.join(segments))
                return 

            # if not all chars consumed or not all segments formed
            if len(segments) == 4 or start == len(s):
                return # dead end/not a valid path, prune
            
            for length in range(1, 4):
                # boundary check
                if start + length > len(s):
                    break

                segment = s[start:start + length]

                if is_valid(segment):
                    segments.append(segment)
                    backtrack(start+length, segments)
                    segments.pop() # pop and try next, pop() rewinds to the state before you made that segment choice, so the next iteration starts clean
                else:
                    break


        backtrack(0, []) # start backtracking from empty state
        return result

# overview of for loop
# "25525511135"
#  ↓ try segment of length 1: "2"
#    ↓ try "5", "55", "525" ...
#  ↓ try segment of length 2: "25"
#    ↓ ...
#  ↓ try segment of length 3: "255"
#    ↓ try "2", "25", "255"  → valid! → recurse
#       ↓ try "5", "55", "511" → 511 > 255, prune ✗
#       ↓ ...


# Trace for "0000"
# backtrack(0, [])
#   segment = "0" ✓ → segments = ["0"]
#     backtrack(1, ["0"])
#       segment = "0" ✓ → segments = ["0","0"]
#         backtrack(2, ["0","0"])
#           segment = "0" ✓ → segments = ["0","0","0"]
#             backtrack(3, ["0","0","0"])
#               segment = "0" ✓, start+length == len(s), len==4 → ADD "0.0.0.0" ✓
#             segments.pop() → ["0","0"]   ← backtrack
#           segment = "00" ✗ leading zero → break
#         segments.pop() → ["0"]           ← backtrack
#       segment = "00" ✗ → break
#     segments.pop() → []                  ← backtrack
#   segment = "00" ✗ → break
# Result: ["0.0.0.0"] ✓

         
        