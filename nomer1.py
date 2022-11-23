#from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
            for i in range(1, len(matrix)): #Берем столбец
                for j in range(1, len(matrix[0])): #Берем строку
                    matrix[i][j] *= min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
            #for i in A: print(i)
            return sum(map(sum, matrix))
# print(Solution.countSquares([
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# ))

'''
Чтобы посчитать единичные квадраты достаточно узнать сумму всех клеток.
Для квадратов 2х2 нужно проверить чтобы в i-1,j i,j-1 i-1,j-1 были 1.
Для этой проверки достаточно найти минимальное число в этой области.
Если будет хотя бы один 0 то к нему прибавится единица и умножится на текущее значение, то есть ничего не изменится
Однако если везде будет 1 тогда минимальным значением будет 1 и к нему прибавится единица и умножится на текущее число,
таким образом значением числа будет 2
Чтобы найти квадраты 3x3 опять же нужно найти минимальное число в i-1,j i,j-1 i-1,j-1 и прибавить к нему единицу
Чтобы получился квадрат 3х3 нужно чтобы окружающие клетки были равны 2,
а они будут ему равны в случае если все они являются частью квадратов 2х2.
Под конец нужно лишь посчитать сумму всех клеток и вывести результат
'''