class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
# Two approaches can be used either to iterate 
# through each value and append its 
# values one by one at the end of input array 
# Second approach is to make an empty output array,
# take each value of input array # and append to the output array.
# Do it twice for concatenation



# Making output array ans
        ans = []
# Since we have to concatenate so we do it twice
        for i in range (2):
            for n in nums:
                ans.append(n)
        return ans
    
# Time complexity ==> O(n)
# Space complexity==> O(n)