## [Medium] Longested Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window perspective:
        # Think of a “window” over part of the string that contains no duplicates.
        # As you move right, expand the window.
        # If a duplicate appears, shrink the left side until the duplicate is gone.
        # Track the MAX window size along the way.
        # O(n) time / O(k) space (k = alphabet size)
        
        left = 0
        chars = set()
        max_len = 0
        l = len(s)

        for right in range(l):
            while s[right] in chars:
                chars.remove(s[left]) 
                left += 1

            chars.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len