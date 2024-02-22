class Solution:
    def fib(self, n: int) -> int:
        now, prev = 0,1
        for _ in range(n):
            tmp = prev + now
            prev = now
            now = tmp
        return now
