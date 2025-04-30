from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # use coins to add up and choose minimal numbers of coins used
        # # until reach the sum of the target amount 
        # # if go over the amount and cannot be exact same, return -1

        # corner case: no amount wanted 
        if amount == 0:
            return 0

        # use queue to store the coin combination from previous step
        queue = deque()
        queue.append((0, 0)) # initialize (cur_amount, cur_numb_coins)
        visited = set()

        while queue:
            cur_amount, cur_numb_coins = queue.popleft()
            # condition to stop
            if cur_amount == amount:
                return cur_numb_coins
            if cur_amount < amount and cur_amount not in visited:
                for coin in coins:
                    queue.append((cur_amount+coin, cur_numb_coins+1))
                    visited.add(cur_amount)
        return -1 # after trying all combinations, not found 















        # # corner case: no amount wanted 
        # if amount == 0:
        #     return 0

        # # use queue to store the coin combination from previous step
        # queue = deque()
        # queue.append((0, 0)) # initialize (cur_amount, cur_numb_coins)

        # while queue:
        #     cur_amount, cur_numb_coins = queue.popleft()
        #     # condition to stop
        #     if cur_amount == amount:
        #         return cur_numb_coins
        #     if cur_amount < amount:
        #         for coin in coins:
        #             queue.append((cur_amount+coin, cur_numb_coins+1))
        # return -1 # after trying all combinations, not found 


        


















        # # use BFS to get combinations of coins one layer by another 

        # # corner case: 0 amount 
        # if amount == 0:
        #     return 0

        # # build a queue for BFS 
        # queue = deque()
        # queue.append((0, 0)) # cur coin sum and steps, which is quantity of coins
        # visited = set()
        # while queue:
        #     cur_sum, cur_step = queue.popleft()

        #     for coin in coins:
        #         # termination case, find sum == the amount 
        #         next_sum = cur_sum + coin
        #         if next_sum == amount:
        #             return cur_step + 1
        #         # normal case: add coin and if sum is not calculated
        #         #   if the sum is calculated before, then this round will make a larger step, so no need
        #         if next_sum < amount and next_sum not in visited:
        #             visited.add(next_sum)
        #             queue.append((next_sum, cur_step+1))
        # return -1 # after the loop, if not found amount, means coins cannot match the amount 








        # # try dynamic programming from bottom to top dp[0] to dp[amount]
        # # the idea is to use 
        # def dp(amount):
        #     if amount == 0:
        #         return 0
        #     if amount < 0:
        #         return float('inf')

        #     for amt in range(amount):
        #         for c in coins:
        #             dp[amt] = min(dp[amt], dp[amt-c] + 1)
            
            




















        # # coins is the list of available coins 
        # # amount is the target sum of selected coins
        # # we want a minimal number of coins to get the amount 

        # # how to get minimal number of coins, we need to select larger coins

        # # corner case: amount is 0
        # if amount == 0:
        #     return 0

        # # pick up the coins less than the amount
        # coin_list = []
        # for c in coins:
        #     if c <= amount:
        #         coin_list.append(c)

        # # corner case: if smallest coin is larger than amount, return -1
        # if coin_list == []:
        #     return -1


        # if len(coin_list) == 1:
        #     if amount < coin_list[0]:
        #         return -1
        #     if amount % coin_list[0] != 0:
        #         return -1

        # # generl case
        # # sort this sub list 
        # coin_list.sort(reverse=True)

        # # pick up the largest coin until one more this coin will make sum greater than amount
        # # then try next smaller coin, keep doing until one more this coin will be greater then amount
        # # keey try coins until no more coin to try

        # # last step to check if the sum is equal to the amount
        # # if yes, return the total coin numbner, if no, return -1
        # memo = dict()

        # def dp(amount):
        #     print('cur memo', memo)
        #     if amount == 0:
        #         return 0
        #     if amount < 0:
        #         return float('inf')
        #     if amount in memo:
        #         return memo[amount]
            
        #     res = float('inf')
        #     for c in coin_list:
        #         res = min(res, dp(amount-c) + 1)
        #         print('cur amount', amount)
        #         print('cur coin', c)
        #         print('cur res', res)
        #         print()
        #     print()
            
        #     # if amount in memo:
        #     #     if res < memo[amount]:
        #     #         memo[amount] = res
        #     memo[amount] = res
        #     return res
        
        # return dp(amount)
            


