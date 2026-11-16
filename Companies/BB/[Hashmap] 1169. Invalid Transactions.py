# either
# 1. amount > 1000
# 2. same name, time1 - time 2 < 60, different city
# add that transaction

# for element in list: 
# parse through every element - name, etc and collect all results
# index the elements in list
# for every element, check condition 1 - check amount in element > 1000 - add the index to list 
# for every pair of element, check condition 2 - xxx - good - add both pairs of indexes into list
# map index to strings/elements 

## TC: O(n^2)
## SC: O(n) - combined and indices

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        combined = []

        for t in transactions:
            name, time, amount, city = t.split(',')
            combined.append([name, int(time), int(amount), city])

        indices = set() # must be a set to avoid adding duplicate elements

        n = len(transactions)

        # condition 1
        for i in range(n):
            name1, time1, amount1, city1 = combined[i]
            if amount1 > 1000:
                indices.add(i)

            # condition 2
            for j in range(n):
                name2, time2, amount2, city2 = combined[j]

                if name1 == name2 and abs(time1 - time2) <= 60 and city1 != city2:
                    indices.add(j)
                    indices.add(i)

        result = [transactions[i] for i in indices]       
        return result     








        