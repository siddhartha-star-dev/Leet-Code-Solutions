class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        l=0
        r=1
        max_profit=0
        while(r<len(prices)):
            profit=prices[r]-prices[l]
            if profit<0:
                l=r
            r+=1
            max_profit=max(max_profit,profit)
        return max_profit
