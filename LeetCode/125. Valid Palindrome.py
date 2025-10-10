class Solution:
    def isPalindrome(self, s: str) -> bool:
        # this question has 3 tasks:
        # lower all letters
        # remove all non-alph chars
        # check forward and backward

        # corner case: emptry string or one letter string
        if len(s) == 0 or len(s) == 1:
            return True

        # use a naive approach 
        # lower all letters and remove non-alph chars 
        letter_list = []
        for l in s:
            if ord(l) >= ord('a') and ord(l) <= ord('z'):
                letter_list.append(l)
            if ord(l) >= ord('A') and ord(l) <= ord('Z'):
                letter_list.append(l.lower())
            if ord(l) >= ord('0') and ord(l) <= ord('9'):
                letter_list.append(l)

        # check forward and backward
        for i in range(len(letter_list)//2):
            # print(i)
            # print(letter_list[i])
            # print(letter_list[-1-i])
            # print()
            if letter_list[i] != letter_list[-1-i]:
                return False
        
        return True