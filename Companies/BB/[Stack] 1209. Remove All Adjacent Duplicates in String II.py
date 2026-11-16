# Why a stack: after you delete a group, the letters on its left and right become neighbours and might form a new group. 
# So for each new letter, the only thing you need to compare with is the **most recent letter you kept**. 
# That’s the top of a stack.

# a → [a,1]
# b → [a,1] [b,1]
# b → [a,1] [b,2]
# b → [a,1] [b,3] → pop → [a,1]
# a → [a,2]          ← the two a's now touch
# result: "aa"

# Think of it like this: you read the string left to right and write a “kept so far” result. Each new letter can only join a group with the letter right before it in that result, which is always the last thing you wrote.
# The key moment: after deleting bbb, the last kept letter is the old a from the beginning. The new a is compared with it, so the two as correctly join up.

# You never need to look further back than the last kept letter, because:

# if the new letter matches it → the group grows
# if it doesn’t → nothing earlier can match through it (it’s in the way)

# Doing this by scanning the string again and again is O(n²). 
# The stack does it in one pass, because popping automatically “re-exposes” the left neighbour.

# Trick: store [char, count], not single chars, so you don’t have to count backwards.


# remove k letters (adjacent, identical) from s repetitively until we cannot
# ccabbbaac O(n^2)
# ccaaac
# ccc
# stack: [char, count]
# scan through all characters in s
# increment the count of each char by order
# once/if the count == k:
# pop that char out of the stack
# else:
# count += 1 for that char
# return s being subsetted by the stack - whatever char and count that are in the stack


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # [[char1, count1], [char2, count2],...,[charn, countn]]
        # stack[]

        stack = []

        for char in s: # O(n)
            if stack and char == stack[-1][0]:
                 stack[-1][1] += 1
                 if stack[-1][1] == k:
                    stack.pop()
            else: # add this char into stack
                 stack.append([char, 1])

        res = ""
        for char, count in stack:
            res += char * count

        # "".join(char * count for char, count in stack)
            
        return res


        




    