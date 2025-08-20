class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # the question asks to remove palindromic sub string everytime, and finally make the given string empty
        # we need to use minimum steps to do so

        # we need to find the palindromic sub string everytime and it does not have to letters as neighbors
        # so, we can pair letters between head and tail 

        # if head letter same as tail letter, remove, if different, shift one position(who to shift and how many steps to shift?), until they meet in the middle
        # corner cases
        if len(s) == 1:
            return 1
        if len(s) == 2 and s[0]!=s[1]:
            return 2
        if len(s) == 2 and s[0]==s[1]:
            return 1

        # if string has one letter only, then return 1
        if 'a' in s and 'b' not in s:
            return 1
        if 'a' not in s and 'b' in s:
            return 1

        # normal case: 'a' and 'b' are in s
        # check if s is not palindromic
        for i in range(len(s)):
            if s[i] != s[-1-i]:
                return 2
        
        # after iteration, this string s is palindromic
        return 1
        