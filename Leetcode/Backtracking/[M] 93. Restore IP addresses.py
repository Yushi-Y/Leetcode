# split the string into 4 parts, all valid (between 0 - 255, no leading zero unless only '0')
# try all possible splits with backtracking - recursively find all possible solutions, if one path of solution does not work, go back to last step ('undo' a step) on the path
# at each step, make a choice by picking 1-3 digits as a segment
# if this choice leads to a valid path, continue recursively
# otherwise, undo this choice and try another
# this way we try all combinations

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        result = []

        def is_valid(segment):
            # if seg starts with 0 and len > 1, false
            # if int > 255, false
            if segment[0] == '0' and len(segment) > 1:
                return False
            return 0 <= int(segment) <= 255

        # start is your current position (index) in the string — it tracks how far you've consumed characters.
        # Every time you pick a segment of length, you advance: start + length
        # segments is ['1', '0', '10', '23'] - list of current segments
        def backtrack(start, segments):
            # assume all segments there and all chars consumed
            if len(segments) == 4 and start == len(s):
                result.append('.'.join(segments))
                return 

            # if not all chars consumed or not all segments formed
            if len(segments) == 4 or start == len(s):
                return # dead end, prune
            
            for length in range(1, 4):
                # boundary check
                if start + length > len(s):
                    break
                    
                segment = s[start:start + length]

                if is_valid(segment):
                    segments.append(segment)
                    backtrack(start+length, segments)
                    segments.pop()
                else:
                    break


        backtrack(0, []) # start backtracking from empty state
        return result

            



         
        