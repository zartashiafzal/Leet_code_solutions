class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        low = 1
        high = num // 2
        
        while low <= high:
            mid = low + (high - low) // 2
            if mid == num // mid and num % mid == 0:
                return True
            elif mid < num // mid:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
