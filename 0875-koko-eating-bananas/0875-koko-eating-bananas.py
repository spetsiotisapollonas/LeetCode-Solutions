class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=sum(piles) 
        ans=high
        while low<=high:
            mid=(high+low)//2
            k=0
            for pile in piles:
                k+=(pile+mid-1)//mid
            if k<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans  