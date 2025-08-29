class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # this question wants us to remove duplicates from this list and keep the unique elements in the relative order. 
        # in-place requires to keep them in the original nums list, instead of holding results in a new list 

        unique_set = set() # keep a set to track 
        avail_spot = 0 # an index to indicate the most left side position of "_" so we can move the next unique number to here. 
        for i in range(len(nums)):
            if nums[i] in unique_set: # this element is duplicated
                nums[i] = '_'
            else: # this element is unique 
                unique_set.add(nums[i])
                # try to find the first '_' and switch 
                for j in range(len(nums)):
                    if nums[j] == '_':
                        nums[j] = nums[i]
                        nums[i] = '_'
        
        return len(unique_set)


        # consider the array is sorted, so we don't need to overkill the list 
        # we can use two indices, slow and fast, slow means the position unqiue element should be written at, fast is the next new elements
        