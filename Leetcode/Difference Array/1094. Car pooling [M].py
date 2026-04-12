# TC: O(N + T), N = stops, T = trips;
# SC: O(N)

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # difference array for all stops
        tracker = [0] * 1001
        for num, start, end in trips:
            tracker[start] += num
            tracker[end] -= num
        
        curr = 0
        for change in tracker:
            curr += change
            if curr > capacity:
                return False
        return True





        