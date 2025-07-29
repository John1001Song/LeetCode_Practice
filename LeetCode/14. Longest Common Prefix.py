class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix should start at the first letter 
        # the common strings should be among all strings
        # solution is to set the iteration step as the shortest string length 
        
        # corner case: 1 string in list, return ""
        if len(strs) == 1:
            return strs[0]

        # find the shortest string length 
        min_len = 201
        for string in strs:
            if len(string) < min_len:
                min_len = len(string)
        
        # corner case: 1 string is empty, so no common 
        if min_len == 0:
            return ""
        # print("shortest string length", min_len)
        # print()
        char_list = []
        for i in range(min_len):
            # print('cur i', i)
            cur_char = set()
            for string in strs:
                cur_char.add(string[i])
                # print(f'cur {string} [{i}] is {string[i]}')
            if len(cur_char) == 1:
                char_list.append(list(cur_char)[0])
            else:
                return ''.join(char_list)

        return ''.join(char_list)