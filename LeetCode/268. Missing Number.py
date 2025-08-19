class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # this question is about given a range, which is the size of the nums
        # this range is determined by the size, like size is 3, then, range is 0-3
        # so, as described, always there is one number missing

        # this nums list is random ordered

        # we can use a math approach to solve it
        # since it should include all numbers, but it misses one
        # the sum of the wanted list can be known ahead
        # we sum up given list, and get the difference, which is the missing number

        range_sum = (0 + len(nums)) * (len(nums)+1) / 2
        cur_sum = sum(nums)
        missing = range_sum - cur_sum
        return int(missing)