class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # we need to remove all elements equal to the given val
        # the remaining elements can be in any order
        # we need to return the length of left elements 

        # writer = 0 # the position a non-val element should place
        # reader = 0 # scan through elements 
        #             # when non-val element found, copy it to writer position, then move writer 

        # while reader < len(nums):
        #     # print(nums, 'val', val)
        #     # print('cur writer', writer)
        #     # print(nums[writer])
        #     # print('cur reader', reader)
        #     # print(nums[reader])
        #     if nums[reader] != val:
        #         nums[writer] = nums[reader]
        #         writer += 1
        #         reader += 1
        #     else:
        #         reader += 1
            
        #     # print()
        
        # return writer
        
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            # when val found, do nothing on k, just move index i 
        
        return k
                
