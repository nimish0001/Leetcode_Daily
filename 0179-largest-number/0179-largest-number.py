class Solution:
    def largestNumber(self, nums):

        nums = list(map(str, nums))

        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1

        nums.sort(compare)

        result = "".join(nums)

        return "0" if result[0] == "0" else result