class Solution(object):
    def findTheDifference(self, s, t):
        for char in t:
            if s.count(char) != t.count(char):
                return char
