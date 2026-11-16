# You are given a string `s` containing words and integers separated by **single spaces**. Rearrange its tokens so that:

# 1. All **words**, read from left to right, are sorted alphabetically. # a to z
# 2. All **integers**, read from left to right, are sorted in **ascending** numerical order.
# 3. The **type of token at each position stays the same**: a position originally containing a word must still contain a word, and a position originally containing an integer must still contain an integer.

# Return the resulting string, with tokens separated by single spaces. Every original token must appear exactly as many times as it did in the input.

# **Example**

# ```text
# s = "pear 12 apple -3 banana 2"
# ```

# The words in alphabetical order are `apple`, `banana`, and `pear`. The integers in ascending order are `-3`, `2`, and `12`.

# Placing them back into the corresponding word and integer positions gives:

# ```text
# "apple -3 banana 2 pear 12"
# ```

### Clarify
# words alphabetically - first letter of the word?
# numbers (more than 1 digit) take up one postion


# **Function Description**

# Complete the function `sortWordsAndNumbers` below.

# `sortWordsAndNumbers` has the following parameter:

# - `string s`: the input string containing words and integers.

# **Returns**

# - `string`: the rearranged string satisfying all three properties.



# **Sample Input 0**

# ```text
# orange 10 apple 2 banana 1
# ```

# **Sample Output 0**

# ```text
# apple 1 banana 2 orange 10
# ```

# **Explanation**

# The word positions are 1, 3, and 5. They receive `apple`, `banana`, and `orange`.

# The integer positions are 2, 4, and 6. They receive `1`, `2`, and `10`. Integers are sorted numerically, so `10` comes after `2`.

# **Sample Input 1**

# ```text
# 8 zebra apple -5 8 banana 0
# ```

# **Sample Output 1**

# ```text
# -5 apple banana 0 8 zebra 8
# ```

# **Explanation**

# The original type pattern is:

# ```text
# integer word word integer integer word integer
# ```

# This pattern is preserved. The words become `apple banana zebra`, and the integers become `-5 0 8 8`. Both occurrences of `8` are retained.

# **Sample Input 2**

# ```text
# dog ant cat ant
# ```

# **Sample Output 2**

# ```text
# ant ant cat dog
# ```

# **Python 3 Starter Code**

# ```python
# #!/bin/python3

import os

#
# Complete the 'sortWordsAndNumbers' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.


### pseducode
# split the string to tokens by single space - ['a', 'b', 1, 2, 3]
# tokens - word or integer - get positions - judge is word/integer - T/F (T, F, F)
# for word - sort them alphabetically - take the first letter of each word and sort the indexes
# for integers - sort ascending
# concatenate them back - make sure that they follow the previous index positions - choose to iterate through the tokens again
# this output a list of tokens and numbers
# join back the tokens and numbers to a single string

def sortWordsAndNumbers(s):
    tokens = s.split()

    words = []
    integers = []

    for token in tokens: # O(n)
        if int(token) == True:
            integers.append(token)
        else:
            words.append(token)

    words.sort() # alphabetically? # O(logn)
    integers.sort() # default ascending? 

    ### sorting algorithm
    # pointer for word, pointer for integer - keep track of indicides of each type
    # move along the string, if the position is a word, we take a word
    # if it is an integer, we take an interger
    word_pointer = 0
    int_pointer = 0
    output_list = []

    for token in tokens: # O(n)
        if int(token) == True:
            output_list.append(integers[int_pointer])
            int_pointer += 1
        else:
            output_list.append(words[word_pointer])
            word_pointer += 1

    return " ".join(output_list)

### TC: O(n) + O(logn) = O(n)
### SC: O(n)
# n is num of tokens in s

    




if __name__ == '__main__':
    s = input()
    result = sortWordsAndNumbers(s)

    output_path = os.environ.get('OUTPUT_PATH')
    if output_path:
        with open(output_path, 'w') as f:
            f.write(result + '\n')
    else:
        print(result)
