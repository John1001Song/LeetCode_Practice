class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # the question wants us to merge two lists in-place and they are non-decreasing order, incrasing or same value at least 
        # we need to append nums2 elements into nums1 list which is given length m+n
        # the result should also be non decreasing order 

        # # corner case 1: both are 0 length
        # if m+n == 0:
        #     nums1 = []
        #     # print('return from corner case 1')
        #     return

        # # corner case 2: no merge from nums2
        if n == 0:
            # nums1 = nums1
            # print('return from corner case 2')
            return

        # corner case 3: no merge from nums1
        if m == 0:
            # nums1 = nums2
            # print('return from corner case 3')
            # print('nums1:', nums1)
            # print('nums2:', nums2)
            for i in range(n):
                nums1[i] = nums2[i]
            return
        

        # print('after coner cases')
        # print('m:', m)
        # print('nums1:', nums1)
        # print('n:', n)
        # print('nums2:', nums2)

        # normal case: merge both with some lengths
        i = m-1
        j = n-1
        k = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            # print('k:', k)
            # print('i:', i)
            # print('nums1:', nums1)
            # print('j:', j)
            # print('nums2:', nums2)
            # print()
        
        # print('after while loop')
        # print('i:', i)
        # print('nums1:', nums1)
        # print('j:', j)
        # print('nums2:', nums2)
        # print('k:', k)
        # print()
        if j < 0:
            return
        else:
            for idx in range(j+1):
                nums1[idx] = nums2[idx]

