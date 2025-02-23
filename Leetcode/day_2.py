# Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # maintain two dictionaries for one-to-one character mappings
        s_to_t_mapping = {}
        t_to_s_mapping = {}

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char not in s_to_t_mapping:
                s_to_t_mapping[s_char] = t_char
            if t_char not in t_to_s_mapping:
                t_to_s_mapping[t_char] = s_char

            if s_to_t_mapping[s_char] != t_char or t_to_s_mapping[t_char] != s_char:
                return False

        return True


# Is Subsequence
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



    
