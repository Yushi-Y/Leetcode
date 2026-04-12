# TC: O(n^2) - so O(n) inside O(n)
# SC: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # every palindrome is mirrored around the center (odd length has one letter in middle, even length has two letters)
        def expand(left, right): # this is O(n)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1, right - left - 1 # length of palindrome 
        # for each index i in len(str):
        #     expand around i # odd length
        #     expand around i, i+1 # even length
        #     if found palindrome longer than previous
              # update start and end index 
        # return s[start:end+1]
        start, end, max_len = 0, 0, 0
        for i in range(len(s)): # this is O(n)
            start1, end1, len1 = expand(i, i) 
            start2, end2, len2 = expand(i, i + 1)
            if len1 > max_len:
                start, end, max_len = start1, end1, len1
            if len2 > max_len:
                start, end, max_len = start2, end2, len2
        return s[start:end + 1]
        