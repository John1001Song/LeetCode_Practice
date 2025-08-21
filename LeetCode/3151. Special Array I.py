class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        # corner case: one element, always true
        if len(nums) == 1:
            return True

        # check neighbors pair
        for i in range(len(nums)-1):
            # determine this pair is even & odd
            # odd + even is odd, so sum//2 should not be 0
            pair = nums[i] + nums[i+1]
            if pair%2 == 0:
                return False
        
        return True