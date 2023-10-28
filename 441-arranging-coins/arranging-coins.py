class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Initialize left and right pointers for binary search
        l, r = 1, n
        # Initialize the result variable to store the final number of full steps
        res = 0
        
        # Binary search loop
        while l <= r:
            # Calculate the middle value of the current search space
            mid = (l + r) // 2
            # Calculate the total number of coins that can be arranged using 'mid' steps
            coins = (mid / 2) * (mid + 1)
            
            # Compare the total coins with the given value 'n'
            if coins > n:
                # If the total coins exceed 'n', reduce the search space (move to the left)
                r = mid - 1
            else:
                # If the total coins do not exceed 'n', update the result and expand the search space (move to the right)
                l = mid + 1
                res = max(mid, res)  # Update the result with the current number of steps
        
        # Return the maximum number of full steps that can be arranged within 'n' coins
        return res