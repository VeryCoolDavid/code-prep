class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price=0
        L=0
        for R in range (1,len(prices)):
            if prices[R]<prices[L]:
                L=R
            
            profit= prices[R] - prices[L]
            price=max(price,profit)
        return price