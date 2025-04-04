class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the sorted half: left or right 
        # always check if the target is the sorted half, then split it into half half
        # repeat until the split half half is one element left to compare with target 

        left = 0
        right = len(nums)-1
        middle = len(nums)//2
        # corner cases
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        # normal cases
        while left <= right:
            # check if current middle is the target 
            if nums[middle] == target:
                return middle

            # check which part is sorted
            if nums[left] <= nums[middle]:
                # left part is sorted
                # then check if target is in left
                if nums[left] <= target <= nums[middle]:
                    right = middle
                    middle = (left+right)//2
                else: 
                    # target is in right part 
                    left = middle+1
                    middle = (left+right)//2
            else:
                # right part is sorted
                # check if target is in this part
                if nums[middle] <= target <= nums[right]:
                    left = middle
                    middle = (left+right)//2
                else:
                    right = middle-1
                    middle = (left+right)//2

        # until this step, no value is equal to target 
        return -1