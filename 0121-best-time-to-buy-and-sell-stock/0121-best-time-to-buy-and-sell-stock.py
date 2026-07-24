class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        min_price=float('inf')
        max_price=-1
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
                max_price=min_price
            if prices[i]>max_price:
                max_price=prices[i]
            best=max(best,max_price-min_price)
        return best

