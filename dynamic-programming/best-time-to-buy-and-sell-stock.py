class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #finding the best time to buy strock 
        #buy low sell high b

        #pointers left and right 
        left = 0
        right = 1 
        maxP = 0 #MAXIMUM profit 

        while right < len(prices):
            if prices[left] < prices[right] :
                profit = prices[right] - prices[left]
                maxP = max(maxP , profit)
            else:
                left = right 
            right += 1 
        return maxP