import random 

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(array):
            # base case: array is 0 or 1 length
            if len(array) <= 1:
                return array
            
            # normal case: split into recursive call, then merge them
            mid = len(array) // 2
            left = merge_sort(array[:mid])
            right = merge_sort(array[mid:])
            
            # print('cur left:', left)
            # print('cur right', right)

            return merge(left, right)

        def merge(left, right):
            # combine left and right arrays 
            merged = []
            i, j = 0, 0

            # iterate both arrays and add the smaller first
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            # after the while loop above, left or right must be used out 
            # so, append current tail to merged list 
            if i < len(left):
                # left has a tail
                merged += left[i:]
            if j < len(right):
                # right tail
                merged += right[j:]
            return merged

        return merge_sort(nums)


















        # def quick_sort(nums, left, right):
        #     # find one pivot by func partition
        #     # call itself twice and feed into parameters by left and right half 
        #     # 
        #     # corner case
        #     if left >= right:
        #         return nums
        #     part_index = partition(nums, left, right)
        #     quick_sort(nums, left, part_index-1)
        #     quick_sort(nums, part_index+1, right)
        #     return nums 

        # def partition(num, left, right):
        #     # this partition func chooses the pivot, moves smaller to left of pivot, 
        #     # and moves larger to right 
        #     # return the index for the pivot 
            
        #     # random indx for pivot 
        #     rand_idx = random.randint(left, right)
        #     # swap this random chosen for pivot with most right side 
        #     nums[rand_idx], nums[right] = nums[right], nums[rand_idx]
        #     pivot = nums[right] # initial pivot chosen at most right 
        #     i = left-1 # boundary for smaller values 
        #     for j in range(left, right):
        #         if nums[j] <= pivot:
        #             i += 1 # add index first, prepare to swap the smaller with un-moved larger 
        #             nums[j], nums[i] = nums[i], nums[j]
        #     # after this loop, we split smaller and larger based on pivot 
        #     # now, put the pivot back to correct position from the most right side 
        #     nums[i+1], nums[right] = nums[right], nums[i+1] # i is the smaller idx, +1 is for larger
        #     return i+1 # return this pivot idx 

        # return quick_sort(nums, 0, len(nums)-1)










        # selective sort 
        # O(n^2) Time limit exceeded
        # for i in range(len(nums)):
        #     min_idx = i
            
        #     for j in range(i+1, len(nums)):
        #         if nums[j] < nums[min_idx]:
        #             min_idx = j
            
        #     nums[i], nums[min_idx] = nums[min_idx], nums[i]
        # return nums

        
        # selective sort 
        # time cost O(n^2)

        # i = 0
        # while i < len(nums)-1:
        #     min_idx = i
        #     j = i+1
        #     while j < len(nums):
        #         print('cur i', i)
        #         print('cur j', j)
        #         print('cur nums', nums)
        #         print()
        #         if nums[j] < nums[min_idx]:
        #             min_idx = j
        #         j += 1
        #     nums[i], nums[min_idx] = nums[min_idx], nums[i]
        #     i += 1
        
            