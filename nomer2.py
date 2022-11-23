class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n: 
            return n
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):       
            print(i%2)    
            if i % 2:
                nums[i] = nums[i // 2] + nums[i // 2 + 1] #Если число нечетное то ему присваивается число в два раза меньше и следующее после него
            else:
                nums[i] = nums[i // 2] #Если число четное то присваивается число в два раза меньше что можно заметить из последовательности вывода в условии

        return max(nums)
#print(getMaximumGenerated(n=input()))