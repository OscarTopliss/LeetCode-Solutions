class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small_value = prices[0]
        large_value = prices[0]

        differences = []

        for price in prices:
            if price < small_value:
                small_value = price
                large_value = price
            if price > large_value:
                large_value = price

            differences.append(large_value - small_value)
        
        return max(differences)
        
        
