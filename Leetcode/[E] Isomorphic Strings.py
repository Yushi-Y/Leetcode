# (Easy) Isomorphic Strings
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

