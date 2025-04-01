class Solution:
    def rob(self, nums: List[int]) -> int:
        # memory dict to store max rob at each index
        memo = {}
        
        def recursive(k):
            # at index k, find out the max rob return 
            # edge base case: when index out of current house list, nothing to rob
            if k >= len(nums):
                return 0
            
            if k in memo:
                return memo[k]

            # neighbor cannot be robbed but need to check its value 
            neighbor = recursive(k+1)
            # cur rob combination
            cur_rob = nums[k] + recursive(k+2)
            memo[k] = max(neighbor, cur_rob)
            
            return memo[k]
        
        # start the recursive from index 0
        return recursive(0)