class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # this question asks for if needle occurs in haystack and return the index of the first occurance, otherwise, return -1. 
        # we need to iterate all characters in haystack. once the first character matches, we start to compare needle with the haystack sub string 
        
        idx_hay = 0
        idx_nee = 0

        while idx_hay < len(haystack):
            # print('cur idx_hay', idx_hay)
            # print('cur idx_nee', idx_nee)
            # print()
            if haystack[idx_hay] != needle[idx_nee]: # they cannot match, reset needle index and move haystack to next 
                idx_nee = 0
                idx_hay += 1
                continue
            else: # they are matched
                # corner case: at the tail of haystack, if the tail is shorter than needle, no need to compare and return -1 
                # print('same char')
                # print('haystack at', idx_hay, haystack[idx_hay])
                # print('needle at', idx_nee, needle[idx_nee])
                # print()
                tail_hay = len(haystack) - idx_hay
                if tail_hay < len(needle):
                    return -1

                # normal case: surfficent haystack to compare with needle    
                while idx_nee < len(needle):
                    # print('in needle while loop')
                    # print('haystack', haystack)
                    # print('needle', needle)
                    if haystack[idx_hay] != needle[idx_nee]:
                        idx_hay = idx_hay - idx_nee + 1
                        idx_nee = 0
                        break
                    else:
                        idx_hay += 1
                        idx_nee += 1
                        # print('idx_hay + 1 ', idx_hay)
                        # try:
                        #     print('haystack', haystack[idx_hay])
                        # except:
                        #     print('out of range, haystack', haystack)
                        # print('idx_nee + 1', idx_nee)
                        # try:
                        #     print('needle', needle[idx_nee])
                        # except:
                        #     print('out of range, needle', needle)
                        # print()
                # if needle index reaches its end, return idx_hay-len(needle)
                if idx_nee == len(needle):
                    return idx_hay-len(needle)
                
                # break in the middle, just continue to next position of haystack
        return -1