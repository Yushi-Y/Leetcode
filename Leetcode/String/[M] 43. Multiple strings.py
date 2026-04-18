# not allowed to use int multiplication
# have to simulate manual multiplication on paper: multiple each digit at the end, sum at correct position and so on

# TC: O(ab)
# SC: O(a+b)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # array of strings as product with size max(a+b) - result
        # reverse num1 and num2 for easier calculation
        # for i in num 1:
            # for j in num2:
                # multiple digits, add to result[i+j]
        # concatenate result array to string

        # edge cases
        if num1 == '0' or num2 == '0':
            return '0'

        a, b = len(num1), len(num2)
        result = [0] * (a + b)

        num1, num2 = num1[::-1], num2[::-1]

        for i in range(a):
            for j in range(b):
                prod = int(num1[i]) * int(num2[j])
                result[i + j] += prod
                # carry it to the next digit
                result[i + j + 1] += result[i + j] // 10 # every digit cannot go over 10
                result[i + j] %= 10 # leave the remainder


        # edge case: remove first zeros in product
        while len(result) > 0 and result[-1] == 0:
            result.pop()

        return ''.join(map(str, result[::-1]))


        
        

        