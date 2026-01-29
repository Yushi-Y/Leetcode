# LeetCode 346 - Moving Average from Data Stream
# Difficulty: Easy
# Companies: Meta/Facebook, Amazon, Google, Microsoft

# Problem Statement
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:
# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.


# Example:
# Input:
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output:
# [null, 1.0, 5.5, 4.66667, 6.0]
# Explanation:
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1);  // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3);  // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5);  // return 6.0 = (10 + 3 + 5) / 3



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        :param size: The size of the sliding window
        """
        # Double-Ended Queue (deque)
        # allows you to add or remove elements from both ends efficiently
        # list is ineffcient if pop from left size (O(n) as shift everything to left)
        self.queue = deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        """
        Add a new value to the stream and return the moving average.
        :param val: The new value to add
        :return: The moving average of the last 'size' values
        """
        self.queue.append(val)
        self.sum += val

        if len(self.queue) > self.size:
            removed = self.queue.popleft()
            self.sum -= removed

        running_avg = self.sum / len(self.queue)
        return running_avg
    
    # TC: O(1); SC: O(size)

