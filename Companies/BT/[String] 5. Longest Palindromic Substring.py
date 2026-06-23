# LeetCode 5 — Longest Palindromic Substring (Medium)
# Given a string s, return the longest palindromic substring in s.
# Example 1

# Input: s = "babad"

# Output: "bab" ("aba" is also valid)
# Example 2

# Input: s = "cbbd"

# Output: "bb"
# Constraints

# 1 <= s.length <= 1000
# s consists of only digits and English letters



# TC: O(n^2) - so O(n) inside O(n)
# SC: O(1)


### Thoughts
# a paindrome 呈现中心左右对称
# for each character, expand from the centre to find the longest palindrome (LP)
# track start and end character indices of the LP found
# return the substring with those indices

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1, right - left - 1 # length of palindrome
        
      
        if not s:
            return ""
        
        # for each index i in len(str):
        #     expand around i # odd length
        #     expand around i, i+1 # even length
        #     if found palindrome longer than previous
              # update start and end index 
        start, end, max_len = 0, 0, 0

        for i in range(len(s)):
            start_odd, end_odd, len_odd = expandFromCenter(i, i) # odd length P
            start_even, end_even, len_even = expandFromCenter(i, i + 1) # even length P

            if len_odd > max_len:
                start, end, max_len = start_odd, end_odd, len_odd
            if len_even > max_len:
                start, end, max_len = start_even, end_even, len_even


        return s[start:end + 1]
            
        

### Alternatively (slightly different)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1 # length of palindrome - use length to find start and end indices later
        
      
        if not s:
            return ""
        
        start, end, max_len = 0, 0, 0

        for i in range(len(s)):
            len_odd = expandFromCenter(i, i) # odd length P
            len_even = expandFromCenter(i, i + 1) # even length P
            max_len = max(len_odd, len_even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]