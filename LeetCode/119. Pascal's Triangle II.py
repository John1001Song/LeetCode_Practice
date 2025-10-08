class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # given the row index, we need to print out the row at that level 
        # so the direct approach is to start from the row 0 and add on until the target row 

        # corner case: row 0, 1
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        cur_row_list = [1,1] # init at row 1
        # normal case: iterate from low rank row to target row 
        for r_idx in range(2, rowIndex+1):
            temp_list = [1]
            for i in range(len(cur_row_list)-1):
                temp_list.append(cur_row_list[i]+cur_row_list[i+1])
            temp_list.append(1)
            cur_row_list = temp_list
        
        return cur_row_list