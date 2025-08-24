class Solution:
    # Instead of literally generating all permutations (exponential!), we can just compare character frequencies for finding permutations.
    # Sliding window idea:
    # Fix window size = len(s1) in s2.
    # Move this window across s2.
    # For each window substring, check if its character counts match s1’s character counts.

    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m > n:
            return False
        
        # Create character frequency arrays (a to z)
        need = [0] * 26
        have = [0] * 26

        # Update need to have all characters in s1
        for char in s1:
            need[ord(char) - ord('a')] += 1

        # First window in s2
        for char in s2[:m]:
            have[ord(char) - ord('a')] += 1
    
        if have == need:
            return True

        # Slide window 
        for i in range(m, n):
            add = ord(s2[i]) - ord('a')
            remove = ord(s2[i-m]) - ord('a')
            have[add] += 1
            have[remove] -= 1
            # next_char = s2[i]
            # initial_char = s2[i-m]
            # have[ord(next_char) - ord('a')] += 1
            # have[ord(initial_char) - ord('a')] -= 1

            if have == need:
                return True

        return False