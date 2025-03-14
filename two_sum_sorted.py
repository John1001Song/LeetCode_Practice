class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Step 1: Initialize a dictionary to store numbers and their indices.
        num_to_index = {}
        
        # Step 2: Loop over each number in nums along with its index.
        for i, num in enumerate(nums):
            complementary = target - num
            if complementary in num_to_index:
                return [num_to_index[complementary], i]
            num_to_index[num] = i
        return []

# what is the output? 
# It returns a list, containing the indexes of numA and numB & numA + numB = target
# 
# are these numbers unique in the nums list? 
# no
