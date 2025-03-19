class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        left_empty = False
        right_empty = False
        # edge case: no plant required
        if n == 0:
            return True
        for i in range(length):
            # print('cur i', i)
            if flowerbed[i] == 0:
                # edge case 1: starting position
                if i == 0:
                    left_empty = True
                else: 
                    # normal case: non starting position
                    if flowerbed[i-1] == 0:
                        left_empty = True
                    else:
                        left_empty = False

                # edge case 2: ending position
                if i == length - 1:
                    right_empty = True
                else:
                    # normal case: non ending positions
                    if flowerbed[i+1] == 0:
                        right_empty = True
                    else: 
                        right_empty = False

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n = n-1
                    if n == 0:
                        return True
            # print('after process, cur flowerbed[i]', flowerbed[i])
        return n == 0 