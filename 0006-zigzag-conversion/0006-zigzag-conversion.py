class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        index = 0
        direction = 1

        for char in s:
            rows[index] += char

            if index == 0:
                direction = 1
            elif index == numRows - 1:
                direction = -1

            index += direction

        return ''.join(rows)