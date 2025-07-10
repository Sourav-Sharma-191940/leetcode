class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bruteforce
        # l = len(prices)
        # max_profit = 0 
        
        # for i in range(l):
        #     for j in range(i+1, l):
        #         if prices[j] - prices[i] > max_profit:
        #             max_profit = prices[j] - prices[i]
                    
        # return max_profit

        max_profit = 0
        minimum = prices[0]
        for price in prices:
            if price < minimum:
                minimum = price
            if price> minimum:
                max_profit = max(max_profit, price - minimum)
        return max_profit


