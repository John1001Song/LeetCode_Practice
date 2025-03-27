class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # put elements into dict key is ele, val is its freq
        freq_dict = dict()
        for ele in nums:
            if ele in freq_dict:
                freq_dict[ele] += 1
            else:
                freq_dict[ele] = 1
        
        # convert this dict to list, then sort this list 
        freq_list = []
        for key, val in freq_dict.items():
            freq_list.append((key, val))
        freq_list.sort(key=lambda x:x[1], reverse=True)
        
        # take out the first k elements
        output = []
        for i in range(k):
            output.append(freq_list[i][0])

        return output



import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the freq into dict
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        # use min heap to keep k elements
        heap = []
        for num, freq in freq_dict.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        # return these k elements from heap
        output = []
        for ele in heap:
            output.append(ele[1])
        return output
        
        