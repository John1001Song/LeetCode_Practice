class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # the question wants us to take all digits out and more left side on, the more 10s to times on 
        # then, add up to get a number and plus 1

        tens = 10**(len(digits)-1) 
        val = 0
        for digit in digits:
            val += digit * tens
            tens = tens//10
        val += 1
        res_list = []
        str_val_list = list(str(val))
        for s in str_val_list:
            res_list.append(int(s))

        return res_list