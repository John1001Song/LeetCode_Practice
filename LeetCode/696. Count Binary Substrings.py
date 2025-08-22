class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # this question wants to count sub strings with same amount of 0s and 1s and these 0s should be continued and 1s are also continued; 
        #   they cannot be separately occured with same amount. 
        # a sub sub string can also count once when its father "sub string" already count one 
        # the challenging part is how to recursively call the same func to count a string and its sub string 

        # compress the string by the length of its sub strings' 0s and 1s
        # so, 001100 becomes [2,2,2] OR 000110 becomes [3,2,1]
        # the shorter length is the sliced count for this pair, (3,2) --> 2 and (2,1) --> 1
        # then, we add up 2 and 1 and get 3 

        # corner case: 1 element, no binary sub strings
        if len(s) == 1:
            return 0
        # corner case: two elements but same numbers
        if len(s) == 2:
            if s[0] == s[1]:
                return 0
            else: # corner case: two elements but diff numbers
                return 1

        # normal case: 0s and 1s are mixed
        # compress 
        freq_list = [] # store frequency of continued 0s and 1s 
        cur_num = s[0]
        cur_count = 0
        for num in s:
            if num == cur_num: # same num, we count
                cur_count += 1
            else: # find a diff num, now, not continued, need to record the contined, then count the new num 
                freq_list.append(cur_count)
                cur_count = 1
                cur_num = num
        freq_list.append(cur_count) # add the last sub string with same num
        # print('freq_list:', freq_list)

        # after compressing the string into frequency list, now, check every freq pair
        count = 0
        for i in range(len(freq_list)-1):
            count += min(freq_list[i], freq_list[i+1])
        
        return count




