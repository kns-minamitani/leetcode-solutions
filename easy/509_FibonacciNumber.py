class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        x = 0
        y = 1
        z = 0
        for _ in range(n-1):
            z = x + y
            x = y
            y = z
        return z