class Solution:
    def climbStairs(self, n: int) -> int:
        # recursively push down and see if the previous steps combinations are tried
        # from n stairs, then check n-1 stairs and n-2 stairs

        # # bottom up DP
        # # small
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2

        # # dp[i] = numb of ways to combine 
        # dp = [0] * (n+1)
        # dp[1] = 1
        # dp[2] = 2

        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[n]







        # Sol 2 dynamic program with memory (no repeating computing)
        
        memo = {} # [numb stairs] = total combination
        
        def recursive_stairs(k):
            if k in memo:
                return memo[k]
            
            # base case
            if k == 1:
                memo[1] = 1
                return 1
            if k == 2:
                memo[2] = 2
                return 2
            
            # recursive steps
            memo[k] = recursive_stairs(k-1) + recursive_stairs(k-2)

            return memo[k]
        
        return recursive_stairs(n)