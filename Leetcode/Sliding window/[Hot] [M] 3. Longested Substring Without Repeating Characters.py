class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window perspective:
        # A “window” over part of the string that contains no duplicates.
        # As you move right, expand the window.
        # If a duplicate appears, shrink the left side until the duplicate is gone.
        # Track the MAX window size along the way.
        # Three steps: Expand, Shrink, Update (see Leetcode notes)
        left = 0
        length = 0
        seen = set()

        for right in range(len(s)):
            # shrink - should be a while loop, not for loop as can keep shirnking several times
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # expand
            seen.add(s[right])

            # update
            length = max(length, right - left + 1)

        return length



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