

## Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
    
        # Create a dictionary of characters in s1 and their counts
        dict_s1 = {}
        for c in s1:
            dict_s1[c] = dict_s1.get(c, 0) + 1

        # Create another dictionary to keep track of the characters and their counts in the sliding window
        dict_window = {}
        for i in range(len(s1)):
            dict_window[s2[i]] = dict_window.get(s2[i], 0) + 1

        if dict_s1 == dict_window:
            return True

        # Use a sliding window approach, set the starting point of two pointers
        left = 0
        right = len(s1)

        # Move the sliding window and check at each step is there is a match of dictionaries
        while right < len(s2):
            dict_window[s2[left]] -= 1
            if dict_window[s2[left]] == 0:
                del dict_window[s2[left]]
            left += 1

            dict_window[s2[right]] = dict_window.get(s2[right], 0) + 1
            right += 1

            if dict_s1 == dict_window:
                return True

        return False    


