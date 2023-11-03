class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        
        while l <= r:
            m = l + (r - l) // 2  # Calculate the midpoint without integer overflow
            if m ** 2 > x:
                r = m - 1
            elif m ** 2 < x:
                l = m + 1
                res = m  # Update the result when m ** 2 < x
            else:
                return m  # Return m when m ** 2 == x
        
        return res  # Return the result after the loop
