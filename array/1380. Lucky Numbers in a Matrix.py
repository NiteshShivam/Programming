'''
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.



https://youtu.be/iUM2dOAOA9s
https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
'''

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = []
        col = []
        for each in matrix:
            row.append(min(each))
        length = len(matrix[0])
        rowl = len(matrix)
        for i in range(length):
            result = -1
            for j in range(rowl):
                result = max(result,matrix[j][i])
            col.append(result)
        result = []
        for i in range(rowl):
            for j in range(length):
                if matrix[i][j]==row[i] and matrix[i][j]==col[j]:
                    result.append(row[i])
        return result







=========================
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = []
        col = []
        for each in matrix:
            row.append(min(each))
        length = len(matrix[0])
        rowl = len(matrix)
        for i in range(length):
            result = -1
            for j in range(rowl):
                result = max(result,matrix[j][i])
            col.append(result)
        result = []
        for each in row:
            if each in col:
                result.append(each)
        return result





=============================
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = []
        col = []
        for each in matrix:
            row.append(min(each))
        length = len(matrix[0])
        rowl = len(matrix)
        for i in range(length):
            result = -1
            for j in range(rowl):
                result = max(result,matrix[j][i])
            col.append(result)
        result = []
        maxM = max(row)
        minC = min(col)
        if maxM==minC:
            return [maxM]
        return result
