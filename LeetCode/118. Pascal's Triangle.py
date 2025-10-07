class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # this question wants us to iterate numbers in a list, which is also in a list, cur list is based on previous list to build 
        
        # corner case: one row
        if numRows == 1:
            return [[1]] 

        # corner case: two row
        if numRows == 2:
            return [[1], [1, 1]] 

        # normal conditions
        out_list = [[1], [1, 1]]
        # to build next level list, it is based on previous list 
        for r_idx in range(2,numRows):
            cur_list = [1]
            for i in range(r_idx-1):
                pre_row_list = out_list[r_idx-1]
                cur_list.append(pre_row_list[i] + pre_row_list[i+1])
            cur_list.append(1)
            out_list.append(cur_list)
        return out_list