# hashset only contains keys, not values
# In a dynamic array, popping an element from the middle forces every subsequent element to shift left, which takes O(N) time
# it can insert in O(1) time, but not remove in O(1) time as it requires to swap with the last element in the array, which means you need to know the index of the current element - motivates the hashmap
# hashmap: {val: index}
# list: [val1, val2, val3]

import random

class RandomizedSet:

    def __init__(self):
        """
        Initializes the RandomizedSet object.
        """
        self.map = {}
        self.list = []

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.map[val] = len(self.list)
        self.list.append(val)
        return True


    def remove(self, val: int) -> bool:
        # edge cases
        if val not in self.map:
            return False

        # get the index to remove
        index = self.map[val]
        last_val = self.list[-1]

        # assign the last element with the index to be removed
        # swap the number to remove with the last element
        self.map[last_val] = index
        self.list[index] = last_val

        self.list.pop()
        del self.map[val]

        return True


    def getRandom(self) -> int:
        ran_val = random.choice(self.list)
        return ran_val
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()