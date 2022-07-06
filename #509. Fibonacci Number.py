class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        fibo = 0
        if n == 1:
            return b
        else:
            for i in range(2, n+1):
                fibo = a+b
                temp = b
                b = fibo
                a = temp

        return fibo
