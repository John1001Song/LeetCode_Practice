class Solution:
    def tribonacci(self, n: int) -> int:
        mem = {0:0, 1:1, 2:1}
        def rec_func(n):
            if n == 0 or n == 1:
                return n
            if n == 2:
                return 1
            if n in mem:
                return mem[n]
            else: 
                cur_sum = rec_func(n-3) + rec_func(n-2) + rec_func(n-1)
                mem[n] = cur_sum
                return cur_sum
        


        return rec_func(n)



class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:               # 0 or 1
            return n
        if n == 2:
            return 1
        a, b, c = 0, 1, 1       # T0, T1, T2
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c
