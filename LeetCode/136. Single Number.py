class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # the pattern here is all elements will show twice except for one element 
        # so we can use a set to track these appearance. If not in set, add into, if in set, remove it

        # corner case: one element
        if len(nums) == 1:
            return nums[0]

        # normal case: multiple elements 
        twice_set = set()
        for n in nums:
            if n not in twice_set:
                twice_set.add(n)
            else:
                twice_set.remove(n)

        return twice_set.pop()

