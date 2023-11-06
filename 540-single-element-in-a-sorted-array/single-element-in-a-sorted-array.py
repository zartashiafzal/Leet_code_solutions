class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l < r:
            mid = l + (r - l) // 2
            if (mid % 2 == 0 and mid + 1 < n and nums[mid] == nums[mid + 1]) or \
               (mid % 2 == 1 and mid - 1 >= 0 and nums[mid] == nums[mid - 1]):
                l = mid + 1
            else:
                r = mid

            if mid - 1 >= 0 and mid + 1 < n and nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
                
        return nums[l]

