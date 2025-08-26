class Solution:
    def isValid(self, s: str) -> bool:
        # based on the requirements, we can use a stack first in last out to operate on these characters
        # when doing the character pair matching, it is ok for now to hard code since its number is limited 

        if len(s)%2 == 1:
            return False 

        stack = []
        left_char_list = ['(', '{', '[']
        right_char_list = [')', '}', ']']

        def is_match(left: str, right: str):
            # print(f'is_match checks {left}, {right}')
            if left == '(':
                if right == ')':
                    return True
                else:
                    return False
            if left == '{':
                if right == '}':
                    return True
                else:
                    return False
            if left == '[':
                if right == ']':
                    return True
                else:
                    return False
            return False
        
        counter = 0 # +1 on left char, -1 on right char

        for char in s:
            # print('cur char:', char)
            if char in left_char_list: # find the left side, push
                stack.append(char)
                counter += 1
            if char in right_char_list:
                counter -= 1
                try:
                    cur_left_char = stack.pop()
                except:
                    return False
                res = is_match(cur_left_char, char)
                # print('is_match result', res)
                if res == False:
                    return False
                
        if counter == 0:
            return True
        else: 
            return False