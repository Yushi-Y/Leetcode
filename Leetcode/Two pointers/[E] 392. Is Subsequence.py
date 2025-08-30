# (Easy) Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # uses two pointers, s_index and t_index, to traverse the strings s and t
        s_index = 0
        t_index = 0

        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1

        #  returns True if all characters in s are found within t while maintaining their relative order
        return s_index == len(s)



    
