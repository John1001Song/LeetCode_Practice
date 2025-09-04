class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # since it is sorted, we can insert or find this target at a position by comparing the value in middle range, then we can meet the requirement log n time complexity
        # in general case, we need to compare the value in middle, if it is smaller than target, we take the right side, if it is larger, take the left side, if it is equal to this target, we find it. 

        # corner case: most left > target, 
        if nums[0] >= target:
            return 0

        # corner ccase: most right < target
        if nums[-1] == target:
            return len(nums)-1
        
        if nums[-1] < target:
            return len(nums)
        
        # normal case: target should be in the list 
        left, right = 0, len(nums)-1
        while left < right: # when the list still has two or more values
            # print('cur left', left)
            # print('cur right', right)
            # print('cur (left+right)//2', (left+right)//2)
            # print()
            if nums[(left+right)//2] == target: # middle one match, 
                # print('middle matched')
                # print()
                return (left+right)//2
            elif nums[(left+right)//2] < target: # middle less than target, we should turn to right part of the list 
                # print('middle smaller')
                # print()
                left = (left+right)//2 + 1
                continue
            else: # middle greater than target, we should turn to left part of the list 
                # print('middle bigger')
                # print()
                right = (left+right)//2 
                continue
        
        # until now, target is not in the list and left is equal to right 
        return left
