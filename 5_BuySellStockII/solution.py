class Solution:
    
    
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        current_sum = 0
        
        if len(prices) == 1:
            return 0
        
        for i in range(len(prices)):
            if i != len(prices) - 1:
                profit += max(prices[i+1] - prices[i], 0)
        
        return profit
