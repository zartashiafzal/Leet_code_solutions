class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}         #hashmap containing key value pairs
        for i,n in enumerate(nums):
            diff=target-n
            if diff in map:
                return[map[diff],i]
            else:
                map[n]=i      # If do not find the value then update the hashmap      
        

# Time complexity ==> O(n)
# Space complexity ==> O(n)  since we created a # dictionary in it                                            