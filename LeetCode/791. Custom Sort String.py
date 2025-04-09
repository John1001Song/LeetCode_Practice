class Solution:
    def customSortString(self, order: str, s: str) -> str:
        tail = list()
        valid_s_dict = dict() #["char"] = freq_numb
        for char in s:
            if char in order:
                # valid_s.append(char)
                valid_s_dict[char] = valid_s_dict.get(char, 0) + 1
            else:
                tail.append(char)
        # print("cur valid_s", valid_s)
        # print("cur valid_s_dict", valid_s_dict)

        output = list()
        for char in order:
            if char in valid_s_dict:
                cur_str = char * valid_s_dict[char]
                output.append(cur_str)
        output += tail
        return "".join(str(x) for x in output)