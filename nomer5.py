#from typing import List
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        dp = [1] * len(prices)
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                dp[i] += dp[i - 1]
        print(dp)
        return sum(dp)
        # В итоге получается спиоск где указывается сколько возможных смежных сочетаний приходится на каждое число
        # Например если текущее число отличается на еденицу от предыдущего то добавляется еще один возможный вариант.
        # А если предыдущее число тоже можно было получить несколькими способами то просто прибавляется еще один вариант к тому что уже есть.
#print(Solution.getDescentPeriods([3,2,1,4]))