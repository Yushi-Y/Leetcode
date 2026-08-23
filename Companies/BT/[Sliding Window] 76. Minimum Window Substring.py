# Problem 2 — LC 76: Minimum Window Substring
# Given strings s and t, return the minimum-length substring of s that contains every character of t including duplicates (if t has two 'A's, the window needs at least two 'A's). 
# If no such substring exists, output an empty line. The answer is guaranteed unique. Target complexity: O(|s| + |t|).
# Input format:
# Line 1: s
# Line 2: t
# Output format:
# The minimum window substring (empty line if none exists)
# Example:
# Input:
# ADOBECODEBANC
# ABC

# Output:
# BANC
# Constraints: 1 ≤ |s|, |t| ≤ 10⁵; uppercase and lowercase English letters.

### ACM
# 输入:
# Line 1: 字符串 s
# Line 2: 字符串 t

# 输出:
# 一行, 最小覆盖子串; 不存在则输出空行

### Thoughts
# sliding window on s
# goal - a dictionary to keep track of letters required in t
# current - another dictionary to track what letters we have so far
# as we move around letters in s, check how aligned current and goal become - check the number of types of characters
# right: expand in s to add letter in
# left: shrink in s to minimise the length of substring

### 注意点
# result = s[left:right + 1] 依然是无条件覆盖——每进一次 while 就把 result 换成当前窗口,不管它是不是更短。
# 手动跑反例:
# s = "BANCAAABC", t = "ABC"
# 右指针扫到 index 3 (C): 窗口 "BANC" 覆盖成立, result = "BANC" ✓ (这是正确答案)
#   收缩后覆盖破坏, while 退出
# 右指针继续扫到 index 8 (C): 窗口再次覆盖, result 被覆盖成 "CAAABC" ✗
#   收缩几步后 result 又被覆盖成 "AABC", "ABC"...

# 最后返回的是最后一次收缩时的窗口,纯属运气好坏——不保证是全局最短

import sys

def min_window(s, t):
    if not s or not t:
        return ""
    
    goal = {}
    current = {}

    # fill goal: count how many times a letter is needed in t
    for l in t:
        goal[l] = goal.get(l, 0) + 1

    # check the number of types of characters in goal as matching criteria
    type_in_goal = len(goal)
    type_to_have = 0

    left = 0
    result = ''

    # expand right by one step 
    for right in range(len(s)):
        # add the right letter to current dict
        current[s[right]] = current.get(s[right], 0) + 1

        # check if that letter matches with goal 
        right_char = s[right]
        if right_char in goal and current[right_char] == goal[right_char]:
            type_to_have += 1

        while type_in_goal == type_to_have: # match
            # update the length of result to be shortest (minimal length substring)
            if result == "" or len(result) > right - left + 1: # intially len(result) = 0
                result = s[left:right + 1]

            # shrink left
            left_char = s[left]
            current[left_char] -= 1

            # check if shrinking left does not matches with goal (move from = to <)
            if left_char in goal and current[left_char] < goal[left_char]:
                type_to_have -= 1

            left += 1

    return result




def main():
    input = sys.stdin.read().splitlines()
    s = input[0]
    t = input[1]
    print(min_window(s, t))

main()