# Classic Two Pointer
# TC O(n) — each iteration moves either left or right, and they can meet at most n times total 
# SC O(1) — only a few variables (left, right, s), no extra data structures

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right] # have to recalculate each loop
        
            if s == target:
                return [left + 1, right + 1]

            elif s < target: 
                left += 1

            else:
                right -= 1

        