class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # we need to find all numbers from lower to upper that are not in the nums list 
        # the output should be list of lists, where each inner list is a range for those missing numbers' range

        # corner case: upper is equal to lower 
        if upper == lower:
            if nums == []:
                return [[lower, upper]]
            return []
        
        if nums == []:
            return [[lower, upper]]

        # normal condition: lower < upper 
        # corner case: nums is empty
        if len(nums) == 0:
            return [lower, upper]

        # normal case: nums is not empty
        # logic is number in nums list is like checkpoint, eventually they can be consider as 
        # lower, nums[0], nums[1], ..., nums[-1], upper
        # we need to give out 
        # [lower+1, nums[0]-1], [nums[0]+1, nums[1]-1], [], ...]
        # special case: nums[x]+1 == nums[x-1]-1, then we can skip
        first_range = [lower, nums[0]-1]
        output_list = []
        if lower != nums[0]:
            output_list.append(first_range)
        for indx in range(len(nums)-1):
            left = nums[indx]
            right = nums[indx+1]
            if left == right-1: # when there is no number in this range, ex: 0, 1
                continue # go to next loop
            output_list.append([left+1, right-1])
        
        if nums[-1] != upper:
            output_list.append([nums[-1]+1, upper])

        return output_list