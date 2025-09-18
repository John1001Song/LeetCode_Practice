class Solution:
    def mySqrt(self, x: int) -> int:
        # the question wants a sqrt value round down to a nearest integer
        # based on math, sqrt value is slightly bigger than half of given number 
        # for a simply try, we can just take half, then add 1 every time until its power of 2 just over the given number 

        # find the number with power 2 just smaller than given x
        cur_base = x//2

        # corner case: small input sqrt is itself
        if x == 0 or x == 1:
            return x

        # corner case: half is the sqrt, return
        if cur_base**2 == x:
            return cur_base

        # print('before while cur base:', cur_base)
        while cur_base**2 > x:
            cur_base = cur_base//2

        # print('after 1st while, cur base:', cur_base)

        while (cur_base+1)**2 <= x:
            cur_base += 1
        
        
        return cur_base