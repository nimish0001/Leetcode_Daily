class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        sign = 1
        result = 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < n and s[i] == ' ':
            i += 1

        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        while i < n and s[i].isdigit():
            digit = int(s[i])

            result = result * 10 + digit
            i += 1

        result *= sign

        return max(INT_MIN, min(result, INT_MAX))