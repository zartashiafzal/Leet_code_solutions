#Brute Force
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1,num+1):
            if i*i ==num:
                return True
            if i*i> num:
                return False
 

#___________ BEST METHOD_____________
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num ==1:
            return True
        l=1
        r= num//2

        while l<=r:
            mid=l+(r-l)//2
            if mid ==num//mid and num%mid==0:
                return True
            elif mid < num//mid:
                l=mid+1
            else:
                r=mid-1
        return False









#___________Method using mid's square___________

#   def isPerfectSquare_2(self, num: int) -> bool:
#         l ,r = 1, num
#         while l <= r:
#             mid = (l +r) // 2
#             if mid * mid > num:
#                 r = mid - 1
#             elif mid * mid < num:
#                 l = mid + 1
#             else:
#                 return True
#         return False