class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j = 0,0
        store = 0
        
        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                store = max(store,profit)
            else:
                i = j #when price is at lowest we wanna move left pointer to that lowest pointer
            j+=1
        return store
        
