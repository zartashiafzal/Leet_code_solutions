class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r= 1,n
        rows=0

    #binary search
        while l<=r:
            mid=(l+r)//2
            coins=(mid/2)* (mid+1)

            if coins > n:
                r=mid-1
            else:
                l=mid+1
                rows=max(mid,rows)
        return rows