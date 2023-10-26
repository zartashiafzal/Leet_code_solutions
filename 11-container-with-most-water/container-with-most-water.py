class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0                     # Initialize the maximum area to 0
        l, r = 0, len(height) - 1   # Initialize two pointers, l and r, at the start and end of the height list

        while l < r:                # Continue the loop until the left pointer is less than the right pointer
            area = (r - l) * min(height[l], height[r])  # Calculate the current area between the two pointers
            max_area = max(max_area, area)    # Update the maximum area if the current area is greater

            if height[l] < height[r]:
                l += 1              # Move the left pointer to the right if the left height is smaller
            else:
                r -= 1              # Move the right pointer to the left if the right height is smaller or equal

        return max_area                  # Return the maximum area found during the traversal


# def maxArea(height):
#     res = 0
#     l, r = 0, len(height) - 1
#     while l < r:
#         area = (r - l) * min(height[l], height[r])
#         res = max(res, area)
#         if height[l] < height[r]:
#             l += 1
#         else:
#             r -= 1
#     return res

# # Example usage
# height = [1,8,6,2,5,4,8,3,7]
# print(maxArea(height))