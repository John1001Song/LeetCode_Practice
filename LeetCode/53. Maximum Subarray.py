class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # corner case: one element, return it
        if len(nums) == 1:
            return nums[0]

        # normal case: 
        # we need to compare at current index i, fresh start a new sub array OR add this element to previous sub array
        # if fresh start sub arrary (one element) is bigger than adding to previous sub array, we start this fresh array
        # if adding this element at index i to previous sub array is larger than fresh singular element, we continue the old sub array

        cur_start = 0
        cur_sum = nums[0]
        best_sum = nums[0] # largest sub array sum
        (best_start, best_end) = (0, 0)

        for i in range(1, len(nums)):
            # print(nums)
            # print('cur index:', i)
            # print(f'nums {i}, {nums[i]}')

            # print('--->before comparison')
            # print('cur_start:', cur_start)
            # print('cur_sum:', cur_sum)
            # print('best_sum:', best_sum)
            # print("cur_sum + nums[i]", cur_sum + nums[i])

            if nums[i] > cur_sum + nums[i]: # fresh start is larger than adding this element to previous sub array
                cur_start = i
                cur_sum = nums[i]
            else: # fresh start is smaller than adding this element to previous sub array
                cur_sum += nums[i]
                        
            best_sum = max(cur_sum, best_sum)

            # print('---->after comparison')
            # print('cur_sum:', cur_sum)
            # print('best_sum:', best_sum)
            # print()

        return best_sum

