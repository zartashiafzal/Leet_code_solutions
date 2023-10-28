#__________Basic function to print fibonacci series__________
    # def fib(n):
    #     a=0
    #     b=1
    #     print(a)
    #     print(b)
    #     for i in range(2,n):
    #         c=a+b
    #         a=b
    #         b=c
    #         print(c)
    # fib(5)

#___________ Now coming towards leetcode solution_________

# # ITERATIVE Solution
# class Solution:
#     def fib(self, n: int) -> int:
#         seen = {0: 0, 1:1}
#         for i in range(2, n+1):
#             seen[i] = seen[i-1] + seen[i-2]
#         return(seen[n])


# RECURSIVE Solution
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return(self.fib(n-1) + self. fib(n-2))