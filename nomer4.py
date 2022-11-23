#from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            # Если найдется цена меньше то она станет ценой покупки
            if prices[i] < buy:
                buy = prices[i]
            # Иначе находим выгоду и назначаем следующую цену покупки
            else:
                profit += prices[i] - buy
                buy = prices[i]
        return profit
#print(Solution.maxProfit(prices = [7,1,5,3,6,4]))