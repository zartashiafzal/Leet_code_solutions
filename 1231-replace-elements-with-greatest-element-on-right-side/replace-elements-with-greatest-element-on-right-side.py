class Solution:
     def replaceElements (self, arr: List[int]) -> List[int]:
         # initial max = -1
         # reverse iteration
         # new max = max (oldmax, arr[i])
        rightMax = -1
# in for loop: -1 initial value
# second -1 = for reverse order
# third -1= for stoping once we get to the beginning of array
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr


# Time complexity: O(n)
# No extra memory used





