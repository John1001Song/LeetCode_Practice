class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # convert column number to corresponding letters
        # need to confirm the formula for this transform. 
        # A --> 1
        # Z --> 26
        # AA --> 26+1
        # AZ --> 26+26
        # BA --> 26+26+1
        # BB --> 26+26+2
        # BZ --> 26+26+26
        # CA --> 26+26+26 + 1

        res = ''
        A_num = ord('A')

        # corner case: one letter 
        if columnNumber <= 26:
            return chr(A_num+columnNumber-1)

        while columnNumber > 0:
            columnNumber -= 1
            cur_letter_num = columnNumber%26
            res = chr(A_num + cur_letter_num) + res 
            columnNumber = columnNumber//26

        

        return res