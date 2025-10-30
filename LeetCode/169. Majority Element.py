class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # find the elements appearing more than n/2 (floor) times, where n is the list length 
        # straightforward way is to build a dict for these elements 
        # then find the one with largest occurance

        # # corner case: 1 element
        # if len(nums) == 1:
        #     return nums[0]

        # # normal case: 
        # nums_dict = dict() # [num] = occurance
        # for num in nums:
        #     if num in nums_dict:
        #         nums_dict[num] += 1
        #     else: 
        #         nums_dict[num] = 1

        # # check the ones more than n/2
        # # corner case: what if two numbers have same occurance
        # larger_pair = (0, 0) # number, occurance
        # for num, occ in nums_dict.items():
        #     if occ > larger_pair[1]:
        #         larger_pair = (num, occ)
        
        # return larger_pair[0]

        # consider the pattern, the majority element should be more than other element 
        # so, we check this and next element, if they are same, counter++, if they are different, counter--, we let the two elements "pop"
        # since the majority is more than half, it can one-to-one pop out with other elements, definitely it will keep at the end round

        counter = 0
        cur_maj = None 
        for ele in nums:
            if counter == 0:
                cur_maj = ele
                counter += 1
            elif ele == cur_maj: 
                counter += 1
            else:
                counter -= 1
                # current majority does not change 
        return cur_maj
