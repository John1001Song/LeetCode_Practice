class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # initialize and high starts backwards
        low, mid, high = 0, 0, len(nums)-1

        # until mid and high reach in the middle 
        while mid <= high:
            # case 1: at mid idx, find value for low idx
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1: # case 2: value for mid idx, check next 
                mid += 1
            else: # case 3: nums[mid] == 2, value for high, found at mid; 
                    # no mid idx+1 because not sure what value to be swapped back from high 
                    # the swapped value needs to checked later
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1



        # i = 0
        # while i < len(nums)-1:
        #     j = 0
        #     while j < len(nums)-1-i:
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        #         j += 1
        #     i += 1
        
        # bubble sort 
        # corner case: 1 element 
        # if len(nums) == 1:
        #     return nums

        # n = len(nums)
        # for i in range(n-1):
        #     for j in range(n-i-1):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]



            

