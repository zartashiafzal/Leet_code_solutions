class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the input list in ascending order
        l = 0  # Initialize left pointer at index 0
        r = k - 1  # Initialize right pointer at index k - 1 (inclusive)
        res = float("inf")  # Initialize result to positive infinity

        # Iterate through the list using the two-pointer approach
        while r < len(nums):
            # Calculate the difference between the elements at the right and left pointers
            difference = nums[r] - nums[l]
            # Update the result with the minimum difference found so far
            res = min(res, difference)
            # Move both pointers to the right to explore the next subarray of size k
            l, r = l + 1, r + 1

        return res  # Return the minimum difference found
