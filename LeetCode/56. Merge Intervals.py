class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the list of intervals first
        # add current interval to output list 
        #     if cur interval left is smaller than previous interval right, merge
        #     else, just append

        # gpt solution
        # sort original list
        intervals.sort(key=lambda x:x[0])

        merged = []
        # interate and merge if necessary
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])
        
        return merged



        # # corner cases
        # if len(intervals) == 0 or len(intervals) == 1:
        #     return intervals
        
        # sorted_list = sorted(intervals, key=lambda x:x[0])
        # output_list = []
        # for cur_interval in sorted_list:
        #     # empty starting
        #     if output_list == []:
        #         output_list.append(cur_interval)
        #         continue
        #     # non starting cases
        #     prev_interval = output_list[-1]
        #     if prev_interval[0] <= cur_interval[0] <= prev_interval[1]:
        #         # overlap
        #         if cur_interval[1] <= prev_interval[1]:
        #             # cur interval is in previous interval
        #             # do nothing
        #             continue
        #         else:
        #             # overal but not within
        #             overlap_interval = []
        #             overlap_interval.append(prev_interval[0])
        #             overlap_interval.append(cur_interval[1])
        #             output_list[-1] = overlap_interval
        #     else:
        #         # no overlap, just append 
        #         output_list.append(cur_interval)
        
        # return output_list