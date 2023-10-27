class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        def fib_helper(n, memo):
            if n in memo:
                return memo[n]
            else:
                fib_val = fib_helper(n - 1, memo) + fib_helper(n - 2, memo)
                memo[n] = fib_val
                return fib_val
        
        memo = {0: 0, 1: 1}  # Memoization dictionary to store computed Fibonacci values
        return fib_helper(n, memo)

# Example usage
sol = Solution()
print(sol.fib(2))  # Output: 1
print(sol.fib(3))  # Output: 2
print(sol.fib(4))  # Output: 3
