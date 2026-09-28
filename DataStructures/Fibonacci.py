class Solution:
    def fibonacci(self,n):

        if n == 0:
            return 0
        elif n == 1:
            return 1

        return self.fibonacci(n-1) + self.fibonacci(n-2)

    def fibonacciNumbers(self, n: int) -> list[int]:
        ls = []
        for i in range(n):
            ls.append(self.fibonacci(i))
        return ls