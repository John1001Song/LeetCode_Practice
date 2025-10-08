class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # the given list is a price trend and we need to find the max difference between two numbers in this list 
        # it means we need to find the minimum and maximum numbers 
        # meanwhile, the difference is calculated from left to right, later - before days, which follows the logic 

        # a naive approach is to have all difference and push them into a list/set, then pop them out for the largest difference 

        # diff_list = []
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         diff_list.append(prices[j]-prices[i])
        
        # # compare all diffs
        # cur_largest_diff = 0
        # for diff in diff_list:
        #     if diff > cur_largest_diff:
        #         cur_largest_diff = diff
        # return cur_largest_diff

        # a good approach is to "sell" today and track the lowest price in history, then find the largest difference 
        lowest_p = 10**4 + 1
        max_diff = 0

        for p in prices:
            if p < lowest_p:
                lowest_p = p
            cur_diff = p - lowest_p
            if cur_diff > max_diff:
                max_diff = cur_diff

        return max_diff