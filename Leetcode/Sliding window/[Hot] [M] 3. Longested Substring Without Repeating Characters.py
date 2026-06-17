# LeetCode 3 — Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Examples:

# s = "abcabcbb" → 3 (the answer is "abc")
# s = "bbbbb" → 1 (the answer is "b")
# s = "pwwkew" → 3 (the answer is "wke" — note "pwke" is a subsequence, not a substring)


### TC: O(n), n = len(s), as in the for loop
### SC: O(k), k is all possible chars (like 26 letters in english), as stored in char_store

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window perspective:
        # A “window” over part of the string that contains no duplicates.
        # As you move right, expand the window.
        # If a duplicate appears, shrink the left side until the duplicate is gone.
        # Track the MAX window size along the way.
        # Three steps: Expand, Shrink, Update
        
        # store all chars visited so far with their latest index - char:index (latest occurance)
        # help o judge if this char is in the currrent window and whether to move left
        char_store = {} 
        max_len = 0
        left = 0

        for right in range(len(s)):
            # have a duplicate
            if s[right] in char_store and char_store[s[right]] > left:
                # move left to remove that duplicated letter
                left = char_store[s[right]] + 1

            # update char store with latest index
            char_store[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len





        # left = 0
        # length = 0
        # seen = set()

        # for right in range(len(s)):
        #     # shrink - should be a while loop, not for loop as can keep shirnking several times
        #     while s[right] in seen:
        #         seen.remove(s[left])
        #         left += 1

        #     # expand
        #     seen.add(s[right])

        #     # update
        #     length = max(length, right - left + 1)

        # return length



# We do shirnk first then expand with a set (while allows no duplicates, so expand first is meaningless). 
# However, if you use a dict/counter instead, you can expand first:
# def lengthOfLongestSubstring(s: str) -> int:
#     left = 0
#     count = {}
#     length = 0

#     for right in range(len(s)):
#         # expand
#         count[s[right]] = count.get(s[right], 0) + 1

#         # shrink
#         while count[s[right]] > 1:
#             count[s[left]] -= 1
#             left += 1

#         # update
#         length = max(length, right - left + 1)

#     return length

# This works because a dict tracks counts, so adding a duplicate makes count[s[right]] = 2, which you can still detect, unlike a set.

# TLDR: The order depends on your data structure. Set → shrink first. Dict/counter → either order works.