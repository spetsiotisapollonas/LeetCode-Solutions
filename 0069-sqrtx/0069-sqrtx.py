class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        low=0
        high=x
        best=float('inf')
        ans=0
        while low<=high:
            mid=low+(high-low)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                high=mid-1
            else:
                low=mid+1
                ans=mid
        return ans       
        