class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # corner case: two lists are empty 
        if len(nums1) == 0 or len(nums2) == 0:
            return [-1]

        res = []

        # we need to iterate all elements in list nums1
        for cur_num in nums1:
            # print('nums1', nums1)
            # print('nums2', nums2)
            # print('cur number', cur_num)
            # find the same number in nums2
            idx = 0
            while idx < len(nums2):
                if cur_num == nums2[idx]:
                    # find the same value 
                    # need to find the next greater 
                    # print('cur num', cur_num)
                    # print('idx', idx)
                    gr_idx = idx+1
                    gr = None
                    while gr_idx < len(nums2):
                        # print('within while')
                        # print('gr_idx', gr_idx)
                        # print(f'nums2[{gr_idx}]')
                        if cur_num < nums2[gr_idx]:
                            gr = nums2[gr_idx]
                            res.append(nums2[gr_idx])
                            break
                        
                        gr_idx += 1

                    if gr == None:
                        # print('no gr found')
                        # print()
                        res.append(-1)

                idx += 1

        return res