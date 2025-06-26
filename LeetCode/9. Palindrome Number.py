class Solution:
    def isPalindrome(self, x: int) -> bool:
        # # convert int to string and compare head and tail one by one 
        # str_num = str(x)
        # index = 0
        # while index < len(str_num):
        #     # cur_value = str_num[index]
        #     paired_index = len(str_num)-index-1 
        #     if str_num[index] != str_num[paired_index]:
        #         return False
        #     index += 1
        # return True
        
        # corner case: negative number is always false
        if x < 0:
            return False

        if x %10 == 0 and x != 0:
            return False

        reversed = 0
        while x > reversed:
            reversed = reversed*10 + x%10 # shift reversed last digit to left, append x last digit 
            x = x//10 # drop last digit on x 
            # print('after shift, x', x)
            # print('after shift, reversed', reversed)

        # print('x', x)
        # print('reversed', reversed)
        if x == reversed or x == reversed//10:
            return True
        else:
            return False
