class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # this question asks for a addition of two strings with binary representation 
        # we can split the string into list full of integers 0s and 1s
        # then add these 0s and 1s with binary rules

        # we need to align two string length
        length = max(len(a), len(b))

        # convert string to list full of integers
        a_list = []
        b_list = []
        
        for i in range(len(a)):
            a_list.append(int(a[i]))
        
        for i in range(len(b)):
            b_list.append(int(b[i]))
        
        if len(a) > len(b):
            temp = [0] * (len(a)-len(b))
            b_list = temp + b_list
        else:
            temp = [0] * (len(b)-len(a))
            a_list = temp + a_list

        # print('original a:', a)
        # print('a list:', a_list)
        # print('original b:', b)
        # print('b list:', b_list)

        addon = 0 # a flag to indicate if the less significant positions have an addon for higher positions
        res_list = []

        for i in range(length):
            cur_digit = 0 # reset cur sum
            cur_digit = a_list[-1-i] + b_list[-1-i] + addon
            if cur_digit == 3:
                cur_digit = 1
                addon = 1
            elif cur_digit == 2:
                cur_digit = 0
                addon = 1
            else: # cur_digit == 1 or 0
                addon = 0 # reset 
            res_list.append(str(cur_digit))

        # the last two digits from a and b add up to additional position
        if addon == 1:
            res_list.append(str(1))
        
        res_list.reverse()

        return "".join(res_list)